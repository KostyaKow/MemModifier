
default: so

so: object
	gcc -shared -o direct.so direct.o

object:
	gcc -c -fpic direct.c
#gcc -c -Wall -Werror -fpic direct.c

clean:
	rm -rf *.swp *.o *.so
