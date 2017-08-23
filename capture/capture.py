#!/usr/bin/env python
# -*- coding: utf-8 -*-

from myo_raw import MyoRaw

import sys
import time
import uuid

import numpy as np
import h5py

emg_data  = []
quat_data = []
acc_data  = []
gyr_data  = []
timestamp = ''

dtype = np.int16

def proc_emg(emg, moving):
	global emg_data
	emg_data.append( emg )

def proc_imu(quat, acc, gyr):
	global quat_data, acc_data, gyr_data
	quat_data.append( quat )
	acc_data.append(  acc  )
	gyr_data.append(  gyr  )

m = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)

m.add_emg_handler(proc_emg)
m.add_imu_handler(proc_imu)

m.connect()

try:
	print "\nSampling..."
	timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
	while True:
		m.run()
except KeyboardInterrupt:
	m.disconnect()
	print "\nDone.\n"

emg_data  = np.array( emg_data,  dtype=dtype )
quat_data = np.array( quat_data, dtype=dtype )
acc_data  = np.array( acc_data,  dtype=dtype )
gyr_data  = np.array( gyr_data,  dtype=dtype )

comments = ''

path = 'samples'

with h5py.File("data.hdf5") as f:

	sample_id = str(uuid.uuid4())
	path = path + '/' + sample_id

	dset = f.create_dataset(
		path + '/comments',
		data=comments
	)
	dset.attrs['timestamp'] = timestamp

	f.create_dataset(
		path + '/emg',
		data=emg_data,
		compression='gzip'
	)

	f.create_dataset(
		path + '/acc',
		data=acc_data,
		compression='gzip'
	)

	f.create_dataset(
		path + '/gyr',
		data=gyr_data,
		compression='gzip'
	)

	f.create_dataset(
		path + '/quat',
		data=quat_data,
		compression='gzip'
	)

