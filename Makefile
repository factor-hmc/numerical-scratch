# Makefile Source: http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/
# .dylib compilation source:
# http://www.xappsoftware.com/wordpress/2012/12/20/how-to-create-a-shared-library-on-mac-os-x-using-gcc/


all: lib/libhellomake.dylib lib/libnumarray.dylib exec/hellomake exec/hellomakesl exec/numarray exec/numarraysl

lib/libhellomake.dylib: src/hellofunc.c
	gcc -dynamiclib -o lib/libhellomake.dylib src/hellofunc.c -Iinc

lib/libnumarray.dylib: src/numarray.c
	gcc -dynamiclib -O3 -o lib/libnumarray.dylib src/numarray.c -Iinc

exec/hellomake: src/hellomake.c src/hellofunc.c
	gcc -c -o obj/hellomake.o src/hellomake.c -Iinc
	gcc -c -o obj/hellofunc.o src/hellofunc.c -Iinc
	gcc -o exec/hellomake obj/hellomake.o obj/hellofunc.o -Iinc

exec/hellomakesl: src/hellomake.c lib/libhellomake.dylib inc/hellomake.h
	gcc -Llib -o exec/hellomakesl -lhellomake src/hellomake.c -Iinc

exec/numarray: src/numarray.c src/main.c
	gcc -c -o obj/numarray.o src/numarray.c -Iinc
	gcc -c -o obj/main.o src/main.c -Iinc
	gcc -o exec/numarray obj/numarray.o obj/main.o -Iinc

exec/numarraysl: src/main.c lib/libnumarray.dylib inc/numarray.h
	gcc -Llib -o exec/numarraysl -lnumarray src/main.c -Iinc

.PHONY: clean

clean:
	rm -rf obj/*.o *~ inc/*~ lib/*.dylib *~ exec/*