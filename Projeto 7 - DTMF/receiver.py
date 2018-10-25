import signalTeste as st
import sounddevice as sd
import math
import numpy
import peakutils
from peakutils.plot import plot as pplot
from matplotlib import pyplot as plt

if __name__ == "__main__":
    SM = st.signalMeu()
    freq_dict = {'0':[941, 1336],
                '1':[697,1209],
                '2':[697, 1336],
                '3':[697, 1477],
                '4':[770, 1209],
                '5':[770, 1336],
                '6':[770, 1477],
                '7':[852, 1209],
                '8':[852, 1336],
                '9':[852, 1447],
                'A':[697, 1633],
                'B':[770, 1633],
                'C':[852, 1633],
                'D':[941, 1633],
                'X':[941, 1209],
                '#':[941, 1477],}
    duration = 1  # seconds
    fs = 44100
    sd.default.samplerate = fs
    sd.default.channels = 1
    myarray = int(duration * fs)
    while True:
        print("-----------------------------------------------------")
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
                    
                