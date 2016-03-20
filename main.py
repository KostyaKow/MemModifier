from pycloak import shellutils
from pycloak.shellutils import ls, join, is_file

def err(s):
   print(s)
   exit(-1)

#str process name -> pid
def find_by_name(s):
   proc_dirs  = ls('/proc')
   for x in proc_dirs:
      if not is_file(join('/proc/', x, '/maps')):
         continue

def is_numeric(s):
   return len(list(filter(lambda c: c not in "1234567890", s))) == 0

class Process:
   def __init__(self, pid=-1, name=None):
      if pid == -1 and !name:
         err("Need either pid or name")
      else if pid == -1 && name is not None:
         self.pid = find_by_name(name)
      else if pid != -1:
         self.pid = pid
      else

   def is_valid(self):
      return self.pid != -1

   def is_running(self):
      if !self.is_valid():
         return False

def main():
   if !shellutils.is_admin():
      print("Needs to be root")
      exit()
