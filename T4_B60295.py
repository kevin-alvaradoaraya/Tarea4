"""
Modelos Probabilísticos de Señales y Sistemas
Tarea 4
Estudiante: Kevin Alvarado Araya
Carnet: B60295
Grupo: 01
""" 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm
from scipy import integrate
from scipy import signal

# Lectura de los .csv con pandas
datos=pd.read_csv("bits10k.csv")

# Lectura de datos como numpa array
bits = np.array(datos.to_numpy()).astype("int")

# Frecuencia 
f = 5000 

# Periodo de la onda
T = 1/f 

# Cantidad de puntos de muestreo
p = 50

# Puntos de muestreo para cada período
tp = np.linspace(0, T, p)

# Onda portadora 
sin = np.sin(2*np.pi*f*tp)

# Gráfica onda portaora
plt.figure(figsize=(10,5))
plt.plot(tp, sin, "r")
plt.title("Onda portadora")
plt.xlabel("Tiempo (s)")
plt.ylabel("Magnitud")
plt.savefig("portadora.png")
plt.close

# Frecuencia de muestreo
fs = p/T 

# Cantidad de bits
N=len(bits)

# Línea temporal para toda la señal Tx
t = np.linspace(0, len(bits)*T, N*p)

# Vector para la señal modulada Tx
senal = np.zeros(t.shape)

# Creación de la señal modulada BPSK
for k, b in enumerate(bits):
  if b==1:
    senal[k*p:(k+1)*p] =  sin
  else:
    senal[k*p:(k+1)*p] = -sin

# Muestra de los primeros bits modulados
pb = 10
plt.figure()
plt.plot(senal[0:pb*p], "g")
plt.title("Muestra de bits modulados")
plt.xlabel("Puntos de muestreo")
plt.ylabel("Magnitud")
plt.savefig("modulacion.png")
plt.close

fig, axs = plt.subplots(2)
fig.suptitle('Concatenación de señales', fontsize=20)
plt.subplots_adjust(hspace=0.5)
axs[0].plot(senal[0:pb*p], "g")
axs[0].set_title("Señal modulada")
axs[0].set(xlabel='Puntos de muestreo', ylabel='Magnitud')
axs[1].plot(bits[0:pb+1], "m", drawstyle='steps-pre')
axs[1].set_title("Bits")
axs[1].set(xlabel='Numero de bits', ylabel='Magnitud')
plt.savefig("concatenacion.png")
plt.close


# Potencia instantánea
Pinst = senal**2

# Potencia promedio 
Ps = integrate.trapz(Pinst,t) / (len(bits)*T)

print("La señal posee una potencia promedio de {} W ".format(Ps))


"""SNR=-2"""
SNR= -2
# Potencia del ruido para SNR y potencia de la señal dadas
Pn = Ps / (10**(SNR / 10))
  
# Desviación estándar del ruido
sigma = np.sqrt(Pn)

# Crear ruido
ruido = np.random.normal(0, sigma, senal.shape)

# Señal recibida
Rx = senal + ruido


# PSD antes del canal
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD, "c")
plt.title("DEP antes del canal ruidoso")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('DEP')
plt.savefig("denisidad(no_SNR).png")
plt.close

# Muestra bits recibidos
pb = 10
fw, PSD = signal.welch(Rx, fs)

# Señal ruidosa y respectiva PSD
fig, axs = plt.subplots(2)
fig.suptitle('Ruido SNR -2 dB', fontsize=20)
plt.subplots_adjust(hspace=0.6)
axs[0].plot(Rx[0:pb*p], "c")
axs[0].set_title("Señal recibida")
axs[0].set(xlabel='Puntos de muestreo', ylabel='Magnitud')
axs[1].plot(fw, PSD, "b")
axs[1].set_title("Densidad espectral")
axs[1].set(xlabel='Frecuencia (Hz)', ylabel='DEP')
plt.savefig("denisidad(-2dB).png")
plt.close

# Aproximación de energía de la onda original
Es = np.sum(sin**2)

# Vector de bits recibidos
bitsRx = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía
for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER1 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER1))




"""Para SNR=-1"""
SNR= -1
Pn = Ps / (10**(SNR / 10))
sigma = np.sqrt(Pn)
ruido = np.random.normal(0, sigma, senal.shape)
Rx = senal + ruido
  
# Muestra bits recibidos
pb = 10
fw, PSD = signal.welch(Rx, fs)

# Señal ruidosa y respectiva PSD
fig, axs = plt.subplots(2)
fig.suptitle('Ruido SNR -1 dB', fontsize=20)
plt.subplots_adjust(hspace=0.6)
axs[0].plot(Rx[0:pb*p], "c")
axs[0].set_title("Señal recibida")
axs[0].set(xlabel='Puntos de muestreo', ylabel='Magnitud')
axs[1].plot(fw, PSD, "b")
axs[1].set_title("Densidad espectral")
axs[1].set(xlabel='Frecuencia (Hz)', ylabel='DEP')
plt.savefig("denisidad(-1dB).png")
plt.close


Es = np.sum(sin**2)
bitsRx = np.zeros(bits.shape)

for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER2 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER2))


"""Para SNR=0"""
SNR= 0
Pn = Ps / (10**(SNR / 10))
sigma = np.sqrt(Pn)
ruido = np.random.normal(0, sigma, senal.shape)
Rx = senal + ruido
  
# Muestra bits recibidos
pb = 10
fw, PSD = signal.welch(Rx, fs)

# Señal ruidosa y respectiva PSD
fig, axs = plt.subplots(2)
fig.suptitle('Ruido SNR 0 dB', fontsize=20)
plt.subplots_adjust(hspace=0.6)
axs[0].plot(Rx[0:pb*p], "c")
axs[0].set_title("Señal recibida")
axs[0].set(xlabel='Puntos de muestreo', ylabel='Magnitud')
axs[1].plot(fw, PSD, "b")
axs[1].set_title("Densidad espectral")
axs[1].set(xlabel='Frecuencia (Hz)', ylabel='DEP')
plt.savefig("denisidad(0dB).png")
plt.close


Es = np.sum(sin**2)
bitsRx = np.zeros(bits.shape)

for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER3 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER3))

"""Para SNR=1"""
SNR= 1
Pn = Ps / (10**(SNR / 10))
sigma = np.sqrt(Pn)
ruido = np.random.normal(0, sigma, senal.shape)
Rx = senal + ruido
  
# Muestra bits recibidos
pb = 10
fw, PSD = signal.welch(Rx, fs)

# Señal ruidosa y respectiva PSD
fig, axs = plt.subplots(2)
fig.suptitle('Ruido SNR 1 dB', fontsize=20)
plt.subplots_adjust(hspace=0.6)
axs[0].plot(Rx[0:pb*p], "c")
axs[0].set_title("Señal recibida")
axs[0].set(xlabel='Puntos de muestreo', ylabel='Magnitud')
axs[1].plot(fw, PSD, "b")
axs[1].set_title("Densidad espectral")
axs[1].set(xlabel='Frecuencia (Hz)', ylabel='DEP')
plt.savefig("denisidad(1dB).png")
plt.close


Es = np.sum(sin**2)
bitsRx = np.zeros(bits.shape)

for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER4 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER4))

"""Para SNR=2"""
SNR= 2
Pn = Ps / (10**(SNR / 10))
sigma = np.sqrt(Pn)
ruido = np.random.normal(0, sigma, senal.shape)
Rx = senal + ruido
  
# Muestra bits recibidos
pb = 10
fw, PSD = signal.welch(Rx, fs)

# Señal ruidosa y respectiva PSD
fig, axs = plt.subplots(2)
fig.suptitle('Ruido SNR 1 dB', fontsize=20)
plt.subplots_adjust(hspace=0.6)
axs[0].plot(Rx[0:pb*p], "c")
axs[0].set_title("Señal recibida")
axs[0].set(xlabel='Puntos de muestreo', ylabel='Magnitud')
axs[1].plot(fw, PSD, "b")
axs[1].set_title("Densidad espectral")
axs[1].set(xlabel='Frecuencia (Hz)', ylabel='DEP')
plt.savefig("denisidad(1dB).png")
plt.close

Es = np.sum(sin**2)
bitsRx = np.zeros(bits.shape)

for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER5 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER4))


"""Para SNR=3"""
SNR= 3
Pn = Ps / (10**(SNR / 10))
sigma = np.sqrt(Pn)
ruido = np.random.normal(0, sigma, senal.shape)
Rx = senal + ruido
  
# Muestra bits recibidos
pb = 10
fw, PSD = signal.welch(Rx, fs)

# Señal ruidosa y respectiva PSD
fig, axs = plt.subplots(2)
fig.suptitle('Ruido SNR 3 dB', fontsize=20)
plt.subplots_adjust(hspace=0.6)
axs[0].plot(Rx[0:pb*p], "c")
axs[0].set_title("Señal recibida")
axs[0].set(xlabel='Puntos de muestreo', ylabel='Magnitud')
axs[1].plot(fw, PSD, "b")
axs[1].set_title("Densidad espectral")
axs[1].set(xlabel='Frecuencia (Hz)', ylabel='DEP')
plt.savefig("denisidad(3dB).png")
plt.close

Es = np.sum(sin**2)
bitsRx = np.zeros(bits.shape)

for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER6 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER6))

# BER vs SNR
BER=[BER1, BER2, BER3, BER4, BER5, BER5]
SNR=[-2, -1, 0, 1, 2, 3]

plt.figure()
plt.plot(SNR, BER, "y")
plt.title("BER vs SNR")
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.savefig("BERvsSNR.png")
plt.close