#from ctypes import cdll, CDLL
from ctypes import *

cdll.LoadLibrary('./direct.so')
direct = CDLL('./direct.so')

pid = 13431
address = 0x1634010
new_val = c_char('k')
n = direct.test(pid, address, new_val)
print('written %s bytes' % n)
