#include <stdio.h>
#include <unistd.h>

int main() {
   char c = 'k';

   while (1) {
      printf("%c\n", c);
      usleep(1000000);
   }
}
