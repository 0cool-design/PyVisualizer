from turtle import left
import pyaudio, threading
import numpy as np
import matplotlib.pyplot as plt

def Td_plot(left_data, right_data):
    #3d plot on the fly
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    plt.tight_layout(pad=2.0, w_pad=10.0, h_pad=3.0)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d(0, len(left_data))
    ax.set_ylim3d(-1, len(left_data))
    ax.set_zlim3d(0, 1)
    ax.view_init(elev=20., azim=-35)
    #ax.plot(left_data, right_data, zs=0, zdir='z', label='curve in (x, y)')
    ax.scatter(left_data, right_data, zs=0, zdir='y', c='r', label='points in (x, z)')
    plt.show()
    


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
    #threading.Thread(target=Td_plot, args=(dataL, dataR)).start()
    lString = "█"*int(peakL*bars)+" "*int(bars-peakL*bars)
    rString = "█"*int(peakR*bars)+" "*int(bars-peakR*bars)
    #print("\rL: [%s] %0.1f" % (lString, peakL) + " R: [%s] %0.1f" % (rString, peakR), end="")
    print("%s█%s"%(lString[::-1], rString))