import signalTeste as st
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin, freqz

def normalize(valor,mi,ma):
    normalized = (valor-mi)/(ma-mi)
    return normalized

freqC = 12000

SM = st.signalMeu()
data, samplerateWMV = sf.read("qdeliciacara.wav")
data = normalize(data,-1,1)
duracao = len(data)/44100

nyq_rate = samplerateWMV / 2.0
width = 5.0/nyq_rate
ripple_dp = 60.0
N, beta = kaiserord(ripple_dp, width)
cutoff_hz = 4000.0
taps = firwin(N, cutoff_hz/nyq_rate, window = ('kaiser', beta))
dataFiltrado = lfilter(taps, 1.0, data)


x1,s1 = SM.generateSin(freqC,1,duracao, 44100)
S = s1+dataFiltrado*s1
#plt.plot(dataFiltrado)
#plt.show()
#plt.plot(S)
#plt.show()
#SM.plotFFT(S,44100)
#SM.plotFFT(dataFiltrado,44100)


#sd.play(data,samplerateWMV)
#sd.wait()