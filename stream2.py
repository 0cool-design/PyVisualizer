import pyaudio, os
import numpy as np



maxValue = 2**16
bars = 35
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=2,rate=44100,
              input=True, frames_per_buffer=1024)
while True:
    data = np.fromstring(stream.read(1024),dtype=np.int16)
    dataL = data[0::2]
    dataR = data[1::2]
    peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue
    peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue
    lString = "█"*int(peakL*bars)+" "*int(bars-peakL*bars)
    rString = "█"*int(peakR*bars)+" "*int(bars-peakR*bars)
    os.system('cls')
    print("\rL: [%s] %0.1f" % (lString, peakL) + " R: [%s] %0.1f" % (rString, peakR), end="")
    #print("%s█%s"%(lString[::-1], rString))