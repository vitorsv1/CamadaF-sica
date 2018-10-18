#Authors - Arthur Olga e Vitor Satyro

import signalTeste as st
import sounddevice as sd
import keyboard as kb
import matplotlib.pyplot as plt

def main():
    print("Começou...")
    Hearing = True
    SM = st.signalMeu()
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
    while Hearing:  
        for k in freq_dict.keys(): #Lendo cada chave do dicionário
            if kb.is_pressed(k): #Se uma chave do freq_dict for pressionada no telcado
                print('You Pressed A Key!')
                x = freq_dict[k.capitalize()] #Deixa a letra pressionada em maiuscula
                x1,s1= SM.generateSin(x[0],10,2,44100)
                x1,s2= SM.generateSin(x[1],10,2,44100)
                s = s1+s2
                sd.play(s) #Tocar as duas frequencias juntas
                sd.wait()
                #plt.plot(s)
                #plt.xlim(0,500)
                #SM.plotFFT(s,44100)
                break
            if kb.is_pressed("esc"): #Para sair do loop usa-se "/"
                Hearing = False 
                break 
            else:
                pass


if __name__ == "__main__":
    main()