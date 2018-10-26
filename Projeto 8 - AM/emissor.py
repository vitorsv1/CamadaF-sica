import signalTeste as st
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin, freqz

def normalize(valor,ma):
    normalized = valor/ma
    return normalized

def lowpassFilter(datas, samplerate):
    nyq_rate = samplerate / 2.0
    width = 5.0/nyq_rate
    ripple_dp = 60.0
    N, beta = kaiserord(ripple_dp, width)
    cutoff_hz = 6000.0
    taps = firwin(N, cutoff_hz/nyq_rate, window = ('kaiser', beta))
    return lfilter(taps, 1.0, datas)
     

freqC = 11000

SM = st.signalMeu()
dataA, samplerateWMV = sf.read("qdeliciacara.wav")
data = []
for i in dataA:
    data.append(i)
stuff = [0]*17500
dataA = data + stuff
data = normalize(dataA,max(dataA))
duracao = len(dataA)/44100
dataFiltrado = lowpassFilter(data,samplerateWMV)
x1,s1 = SM.generateSin(freqC,1,duracao, 44100)
S = dataFiltrado*s1

#plt.figure()
#plt.title("Audio original no tempo")
#plt.plot(dataA)
#plt.figure()
#plt.title("Audio normalizado no tempo")
#plt.plot(data)
#plt.figure()
#plt.title("Audio filtrado no tempo")
#plt.plot(dataFiltrado)
#plt.figure()
#plt.title("Audio modulado no tempo")
#plt.plot(S)
#plt.show()

#SM.plotFFT(dataA,samplerateWMV)
#SM.plotFFT(data,samplerateWMV)
#SM.plotFFT(dataFiltrado,samplerateWMV)
SM.plotFFT(S,samplerateWMV)

sd.play(S,samplerateWMV)
sd.wait()