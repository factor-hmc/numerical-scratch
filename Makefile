IDIR =inc
CC=gcc
CFLAGS=-I$(IDIR)
LFLAGS=-dynamiclib

SDIR=src
ODIR=obj
LDIR =lib

LIBS=-lm

_DEPS = hellomake.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_LSRC = hellofunc.c
LSRC = $(patsubst %,$(SDIR)/%,$(_LSRC))

_OBJ = hellomake.o hellofunc.o
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))



$(ODIR)/%.o: $(SDIR)/%.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

hellomake: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)
	make $(LDIR)/lib$@.dylib

$(LDIR)/libhellomake.dylib: $(LSRC)
	$(CC) $(LFLAGS) -o $@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ $(LDIR)/*.so *~ $(LDIR)/*.dylib *~ hellomake