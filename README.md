# Modelos Probabilísticos de Señales y Sistemas

# Tarea 3

# Estudiante: Kevin Alvarado Araya

# Carnet: B60295

# Grupo: 01

Punto 1

Se asigna una onda portadora senoidal (figura "portadora.PNG) la cual se utiliza para la modulación BPSK de los valores binarios del archivo “bits10K.csv”. Dado que los archivos son binarios,  se representan como un tren de pulsos de longitud variable con con valor máximo en 1 y mínimo en cero. La modulación BPSK transmite los valores en 1 como una función seno y los 0 como una función –seno (figura “modulación.PNG”). La concatenación de estos comportamientos para los primeros 10 bits se observa en la figura “concatenacion.PNG”. 

Punto 2

Para esta señal se calcula una potencia promedio de 0.4900009800019598 W.

Punto 3 y Punto 4

Para un rango SNR entre los -2dB y 3dB se grafica el comportamiento de la señal a través de un canal bajo esas condiciones. Las figuras “SNR(-2db).PNG”, “SNR(-1db).PNG”, “SNR(0db).PNG”, “SNR(1db).PNG”, “SNR(2db).PNG” y “SNR(3db).PNG” además de mostrar el comportamiento de la señal trasmitida, también contempla la densidad espectral de potencia (DEP o PSD). 

Para los casos  de SNR = -2db y -1dB las distorsión es mayor dado que la potencia del ruido es mayor a la potencia de la señal. Cabe destacar que en todos los casos las gráficas DEP son iguales dado que se trata de la misma señal con una frecuencia de 5 kHz por lo tanto, la potencia de la señal se va a distribuir principalmente entre 0 Hz y 5 kHz con un magnitud máxima 10x10^-4. Si comparamos los valores de la DEP a través del canal ruidos con la DEP de la señal antes del canal (figura  densidad_senal.PNG) se determina que la distribución y valores de potencia se mantienen antes como después del canal ruidoso.

Punto 5

Para SNR= -2 hay  un total de 7.0 errores en 10000 bits para una tasa de error de 0.0007.

Para SNR= -1 hay  un total de 3.0 errores en 10000 bits para una tasa de error de 0.0003.

Para SNR= 0 hay  un total de 1.0 errores en 10000 bits para una tasa de error de 0.0001.

Para SNR= 1 hay  un total de 0.0 errores en 10000 bits para una tasa de error de 0.0.

Para SNR= 2 hay  un total de 1.0 errores en 10000 bits para una tasa de error de 0.0.

Para SNR= 3 hay  un total de 0.0 errores en 10000 bits para una tasa de error de 0.0.

Cabe destacar que el por definición es variable, por lo tanto, para cada vez que ejecuta el script los valores tienden a variar pero el comportamiento es el mismo, para SNR menores a 0 dB tienden a haber más errores y para valores SNR mayores a 0 dB la tasa de error fue de 0 en la mayotoría de las iteraciones.

Punto 6

En la figura “BERvsSNR.PNG” se puede apreciar mejor la tendencia a la disminución en la taza de error conforme SNR toma valore más positivos. Esto corresponde a que la relación entre la potencia de la señal y la potencia del ruido es mayor a 1 para valores SNR mayores a 0 dB.
