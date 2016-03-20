from pycloak import shellutils as u
import time

sleep_time = 0.2

def err(s):
   print(s)
   exit(-1)

#str process name -> pid
def find_by_name(name):
   proc_dirs  = u.ls('/proc')
   for path in proc_dirs:
      if not u.is_file(u.join('/proc', path, 'maps')):
         continue
      p = Process(path)
      exe_path = p.get_exe_path()
      if not p.is_running() or not exe_path:
         continue
      fname = u.get_file_name(exe_path)
      if fname == name:
         return p
   return None

class Process:
   def __init__(self, pid=-1):
      self.mmaps = None
      self.pid = pid
      self.bad = False
      if not is_numeric(pid):
         self.bad = True
   def is_valid(self):
      return self.pid != -1 and not self.bad
   def is_running(self):
      if not self.is_valid():
         return False
      return u.is_dir(u.join('/proc', self.pid))
   def get_exe_path(self):
      if not self.is_running(): 
         return None
      try:
         path = u.expand_link(u.join('/proc', self.pid, 'exe'))
      except:
         return None
      if u.file_exists(path):
         return path
      else:
         return None
   def get_working_dir(self):
      if not self.is_running():
         return None
      path = u.expand_link(u.join('/proc', self.pid, 'cwd'))
      if u.file_exists(path):
         return path
      else:
         return None
   def parse_mmaps(self):
      maps = []
      mapsStr = u.read_file(u.join('/proc', self.pid, 'maps')).strip()
      entries = mapsStr.split('\n')
      for entry in entries:
         lst = entry.split(' ')
         item = {
            'region'       : lst[0],
            'permissions'  : lst[1],
            'offset'       : lst[2],
            'device'       : lst[3],
            'inode'        : lst[4]
         }
         maps.append(item)
      return maps

class MemoryMap:
   def __init__(self):
      #memory
      self.start = self.end = 0 #ulong
      #permissions 
      self.readable = self.writable = self.executable = self.shared = False #bool

      #file data
      self.offset = 0 #ulong 
      self.deviceMajor = self.deviceMinor = 0 #uchar
      self.inodeFnum = 0 #ulong inodeFileNumber
      self.pathname = self.fname = ''

      client_start = 0 #ulong
      
   def find(proc, data, pattern):
      pass #kk TODO

def main():
   if not u.is_admin():
      print("Needs to be root")
      exit()

   csgo = None
   while True:
      time.sleep(sleep_time)
      csgo = find_by_name('csgo_linux')
      if csgo is not None:
         break
   print("CSGO: %s %s", csgo.pid, csgo.get_exe_path())

   client = MemoryMap()
   while client.start == 0:
      if not csgo.is_running():
         err('Exited game before we found cilent')

      csgo.parse_mmaps()
      for mmap in csgo.maps:
         if mmap.fname == 'client_client.so' and mmap.executable:
            print('client_client.so: [%s] [%s] [%s]' % (mmap.start , mmap.end, mmap.pathname))
            client = mmap
            break
      time.sleep(sleep_time)

   
#main()

def is_numeric(s):
   return len(list(filter(lambda c: c not in "1234567890", s))) == 0

