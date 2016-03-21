#from ctypes import cdll, CDLL
from ctypes import *

cdll.LoadLibrary('./direct.so')
direct = CDLL('./direct.so')

pid = 12688
address = 0x1dd3010
new_val = 'z'
n = direct.test(pid, address, new_val)
print('written %s bytes' % n)
