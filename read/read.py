#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import h5py

import matplotlib.pyplot as plt

file    = 'data.hdf5'

group = 'samples'

with h5py.File( file ) as f:

	for s in f[group]:

		emg = f[ group + '/' + s + '/emg']

		print emg.shape
		print emg[6].mean()

		plt.plot( emg )
		plt.show()