import signalTeste as st
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin, freqz

while True:
        print("start")
        myrecording = sd.rec(myarray, samplerate=fs, channels=1)
        sd.wait()
        #print((myrecording))
        #sd.play(myrecording) 
        #sd.wait()
        s = []
        for i in myrecording:
            s.append(i[0])
        peaks = SM.getFFT(s,44100)
        
        for i in range(len(peaks)-1):
            for j in freq_dict:
                #if peaks[i]==j[0] and peaks[i+1]==j[1]:
                z = freq_dict[j]
                if math.isclose(peaks[i], z[0], rel_tol=0) and math.isclose(peaks[i+1], z[1], rel_tol=0):
                    print("Tecla apertada " + j)
                    SM.plotFFT(s,44100)