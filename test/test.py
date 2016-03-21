#from ctypes import cdll, CDLL
from ctypes import *

cdll.LoadLibrary('./direct.so')
direct = CDLL('./direct.so')

pid = 20570
address = 0xe37010
new_val = c_char(b'f')
n = direct.test(pid, address, new_val)
print('written %s bytes' % n)
