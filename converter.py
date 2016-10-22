import scipy.io.wavfile, math, numpy
import numpy as np

from scipy.signal import hilbert

baseband = scipy.io.wavfile.read("lindsey.wav")[1]
baseband = baseband / float(np.max(baseband))
print(baseband.shape)
carrier = np.sin(np.linspace(0, 2*np.pi*40690*baseband.shape[0]/96000, num=baseband.shape[0]))
carriercos = np.cos(np.linspace(0, 2*np.pi*40000*baseband.shape[0]/96000, num=baseband.shape[0]))

print carrier.shape
print baseband.shape
#print carrier[0:100]
output = baseband*carrier[:, None]
#output -= np.real(hilbert(baseband)* carriercos[:, None])

scipy.io.wavfile.write("out.wav", 96000, output)