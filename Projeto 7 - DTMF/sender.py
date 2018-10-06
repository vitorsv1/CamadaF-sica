import signalTeste as st
import sounddevice as sd
from collections import defaultdict

if __name__ == "__main__":
    SM = st.signalMeu()
    penis = []
    sd.default.samplerate =  44100
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
    while True:
        n = input("Qual numero/letra? ")
        try:
            x = freq_dict[n.capitalize()] #Pegar as duas frequencias relativas ao valor
            #Existem casos de A B C D X e #
        except:
            x = [120,560] #Mensagem de erro caso seja inputado um numero nao presente no dicionario
            print("Esse número/letra não existe")
        #print(x[0])
        x1,s1= SM.generateSin(x[0],10,0.35,44100)
        x1,s2= SM.generateSin(x[1],10,0.35,44100)
        s = []
        for i in range(len(s1)):
            s.append(s1[i]+s2[i])
        sd.play(s) #Tocar as duas frequencias juntas
        sd.wait()
    
    print('sugma')