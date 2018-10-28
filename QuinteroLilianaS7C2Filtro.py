import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

from scipy.fftpack import fft, fftfreq, ifft


wave= wav.read('violin.wav')


n= len(wave[1])

transformada=abs((fft(wave[1])/n))
frecuencia=fftfreq(n, 1/float((wave[0])))

plt.figure()
plt.plot(frecuencia, transformada)
plt.savefig('violin.pdf')

wave2= wave[1]
fiosehfñewfguerslghlseiru

def t(wave2,frecuencia):
	for i in range (len(wave2)):
		if (abs(frecuencia[i]) < 2000):
			wave2[i]=0
	return wave2

w= t(wave2,frecuencia)
#t2=abs(fft(wave2)/n)

plt.figure()
plt.plot(frecuencia, w)
plt.plot(frecuencia, transformada)
plt.savefig('ViolinFiltro.pdf')

inversa= ifft(wave2)

#wav.write('violinfiltrado.wav', 1/float(wave[0]), inversa)

