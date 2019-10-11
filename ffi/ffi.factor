USING: alien alien.c-types alien.libraries alien.syntax ;
IN: numerical-scratch.ffi

<< "hellomake" "../lib/libhellomake.dylib" cdecl add-library >>

LIBRARY: hellomake

FUNCTION: void myPrintHelloMake ( )