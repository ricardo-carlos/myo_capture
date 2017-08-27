# myo_capture

Use Python to acquire data from Thalmic Labs' Myo and save it to HDF5.

# Firmware

In order to get the accelerometer to sample at 200Hz I had to downgrade to [firmware version 0.8.18](https://s3.amazonaws.com/thalmicdownloads/firmware/myo-firmware-0.8.18-revd.hex). Just follow [the instructions](https://www.myo.com/firmwareupdate).

# Device permissions

Run this to set the device permissions for the USB dongle on GNU/Linux systems:
	
`$ sudo usermod -aG dialout $USER `

# Dependencies

- NumPy 
- h5py

`$ pip install numpy h5py `

I used [dzhu's myo-raw](https://github.com/dzhu/myo-raw) to get data from the sensor, just changed the IMU's sampling rate and included his code.

# Data capture

Just run capture/capture.py and press ^C to stop.

# Reading data

It might be a good idea to install [HDFView and the command line utils](https://support.hdfgroup.org/downloads/) to work with HDF5 files.

`$ sudo apt-get install hdf5-tools hdfview `

Check the example in read/read.py to work with this format from python. 

