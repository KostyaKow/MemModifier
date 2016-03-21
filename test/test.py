from ctypes import cdll, CDLL

cdll.LoadLibrary('./direct.so')
direct = CDLL('./direct.so')

direct.test1(11, 5)
