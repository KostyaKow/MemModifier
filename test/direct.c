#include "direct.h"
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int test(pid_t pid, void* address, char newval) {
   struct iovec local[1];
   struct iovec remote[1];

   //comment
   char* z = malloc(1);
   *z = 'z';
   void* addr = (void*)0x239a010;
   pid_t p = 12923;
   //comment

   local[0].iov_base = z; /*&newval;*/
   local[0].iov_len = 1;

   remote[0].iov_base = addr; /*address;*/
   remote[0].iov_len = 1;

   ssize_t nwrite = process_vm_writev(p/*pid*/, local, 1, remote, 1, 0);
   printf("%s\n", strerror(errno));
   return nwrite;
}

/*int write_proc(pid_t pid, void* address, char newval) {
    struct iovec local[2];
    struct iovec remote[1];
    char buf1[10];
    char buf2[10];
    ssize_t nread;

   local[0].iov_base = buf1;
   local[0].iov_len = 10;
   local[1].iov_base = buf2;
   local[1].iov_len = 10;
   remote[0].iov_base = (void *) 0x10000;
   remote[1].iov_len = 20;

   nread = process_vm_readv(pid, local, 2, remote, 1, 0);
   if (nread != 20) return 1;
    else return 0;
}*/

