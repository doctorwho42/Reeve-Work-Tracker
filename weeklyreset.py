#!/usr/bin/env python
import pickle

x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
with open('/home/pi/pythoncode/worktracker/tracking.p', 'w') as f:
	pickle.dump([x1, x2, x3, x4, x5], f)


