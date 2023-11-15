#%%
import matplotlib.pyplot as plt
import helpers
import numpy as np
import os, sys, pathlib

sys.path.append(os.path.abspath('./comm'))
import skcomm as skc

plt.style.use('noelle.mplstyle')
plt.ion()

sig = skc.signal.Signal(n_dims=2)
sig.symbol_rate = 100
sig.generate_bits(n_bits=300)
sig.bits[1] = np.zeros(sig.bits[0].size)
sig.bits[1][int(sig.bits[0].size/2)] = True
sig.constellation = np.asarray([-1,1])
sig.mapper()
up = 16
shape = 'rc'
ro = 0.5
sig.pulseshaper(upsampling=up, pulseshape=shape,roll_off=ro)

sig.plot_eye(dimension=0,fNum=1,tit='Augendiagramm')
n_plot_symbols = 10
sig.plot_signal(boundaries=[0,n_plot_symbols*up],dimension=0,fNum=2,tit='Singal nach Pulsformung')
plt.stem(skc.utils.create_time_axis(sample_rate=sig.sample_rate[0],n_samples=n_plot_symbols*up)[::up], sig.symbols[0][:n_plot_symbols],markerfmt='oC1',basefmt='k',linefmt='k')

sig.plot_signal(boundaries=[int(sig.samples[1].size/2-up*10), int(sig.samples[1].size/2+up*10)], dimension=1,fNum=3,tit='Impulsantwort Pulsformer')
sig.plot_spectrum(dimension=1,fNum=4,tit='Frequenzgang Pulsformer')

plt.figure(5)
plt.stem(skc.utils.create_time_axis(sample_rate=sig.sample_rate[0],n_samples=n_plot_symbols*up)[::up], sig.symbols[0][:n_plot_symbols],markerfmt='oC1',basefmt='k',linefmt='k')





