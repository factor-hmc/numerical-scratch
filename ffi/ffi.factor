USING: alien alien.c-types alien.libraries alien.syntax ;
IN: numerical-scratch.ffi

<< "libhellomake" "../lib/libhellomake.dylib" cdecl add-library >>

LIBRARY: libhellomake

FUNCTION: void myPrintHelloMake ( )