#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
   volatile char *c = malloc(1);
   *c = 'k';
   
   while (1) {
      printf("%c\n", *c);
      usleep(3000000);
      printf("%p\n", (void*)c);
   }
}
