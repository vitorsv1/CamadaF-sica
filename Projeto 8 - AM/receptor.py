import signalTeste as st
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin, freqz

duration = 5
fs = 44100
freqC = 9000
SM = st.signalMeu()

while True:
        print("start")
        myrecording = sd.rec(int(duration*fs), samplerate=fs, channels=1)
        sd.wait()
        
        sd.play(myrecording) 
        sd.wait()
        s = []
        for i in myrecording:
            s.append(i[0])
        print(s)
        x1,s1 = SM.generateSin(freqC,1,len(s)/44100, 44100)
        