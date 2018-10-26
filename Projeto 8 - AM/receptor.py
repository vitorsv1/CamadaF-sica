import signalTeste as st
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin, freqz

duration = 5
fs = 44100
freqC = 11000
SM = st.signalMeu()

def lowpassFilter(datas, samplerate):
    nyq_rate = samplerate / 2.0
    width = 5.0/nyq_rate
    ripple_dp = 60.0
    N, beta = kaiserord(ripple_dp, width)
    cutoff_hz = 6000.0
    taps = firwin(N, cutoff_hz/nyq_rate, window = ('kaiser', beta))
    return lfilter(taps, 1.0, datas)
     

while True:
        print("start")
        penis = input("Começa")
        myrecording = sd.rec(int(duration*fs), samplerate=fs, channels=1)
        sd.wait()
        
        #sd.play(myrecording) 
        #sd.wait()
        s = []
        for i in myrecording:
            s.append(i[0])
        #print(s)
       
        s = s + [0]*17500
        x1,s1 = SM.generateSin(freqC,1,len(s)/44100, 44100)
        
        y = s*s1
        dataFiltered = lowpassFilter(y,fs)
        
        
        #plt.plot(s)
        #plt.show()
        #plt.plot(y)
        #plt.show()
        #SM.plotFFT(s,fs)
        SM.plotFFT(dataFiltered,fs)
        sd.play(dataFiltered)
        sd.wait()
