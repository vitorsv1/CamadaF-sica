import signalTeste as st
import sounddevice as sd

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
    print("start")
    myrecording = sd.rec(myarray, samplerate=fs, channels=1)
    sd.wait()
    print((myrecording))
    sd.play(myrecording) 
    sd.wait()
    s = []
    for i in myrecording:
        s.append(i[0])
    SM.plotFFT(s,44100)