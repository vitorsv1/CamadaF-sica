
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
import peakutils
from peakutils.plot import plot as pplot

class signalMeu:
    def __init__(self):
        self.init = 0
        

    def generateSin(self, freq, amplitude, time, fs):
        n = time*fs
        x = np.linspace(0.0, time, n)
        s = amplitude*np.sin(freq*x*2*np.pi)
        return (x, s)

    def calcFFT(self, signal, fs):
        # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
        N  = len(signal)
        W = window.hamming(N)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal*W)
        return(xf, np.abs(yf[0:N//2]))

    def plotFFT(self, signal, fs):
        x,y = self.calcFFT(signal, fs)
        #indexes = peakutils.indexes(y, thres=0.2, min_dist=100)
        #print(indexes)
        #plt.plot(signal)
        #plt.xlim(0,1000)
        #plt.figure(figsize=(10,6))
        #pplot(x, y, indexes)
        #plt.title('First estimate')
        #plt.xlim(0,2200)
        #plt.figure()
        plt.plot(x, np.abs(y))
        plt.title('Fourier')
        plt.show()
        
    def getFFT(self, signal, fs):
        x,y = self.calcFFT(signal, fs)
        indexes = peakutils.indexes(y, thres=0.2, min_dist=100)
        print(indexes)
        return indexes

if __name__ == "__main__":
    SM = signalMeu()
    penis = []
    loop = True
    numbers = [[941, 1336],[697,1209],[697, 1336],[697, 1477],[770, 1209],[770, 1336],[770, 1477],[852, 1209],[852, 1336],[852, 1447]]
    sd.default.samplerate =  44100
    while loop:
        n = input("Qual numero? (Digite s para sair): ")
        if (n == 's'):
            loop = False
            break
        else:
            x = numbers[int(n)] #Pegar as duas frequencias relativas ao valor
            #print(x[0])
            x1,s1= SM.generateSin(x[0],10,0.35,44100)
            x1,s2= SM.generateSin(x[1],10,0.35,44100)
            s = []
            for i in range(len(s1)):
                s.append(s1[i]+s2[i])
            sd.play(s) #Tocar as duas frequencias juntas
            sd.wait()
    