#ifndef DIRECT_H_INCLUDE
#define DIRECT_H_INCLUDE

#include <sys/uio.h>
//extern int write_proc(pid_t pid, void*address);
extern int test(pid_t pid, void* address, char newval);

#endif //DIRECT_H_INCLUDE
