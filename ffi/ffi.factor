USING: alien alien.c-types alien.libraries alien.syntax environment kernel ;
IN: numerical-scratch.ffi

<<
! "/Users/nandeekanayak/Documents/College/Senior Year/Fall 2019/CS 183/numerical-scratch/lib"
! [ "LD_LIBRARY_PATH" set-os-env ] [ "DYLD_LIBRARY_PATH" set-os-env ] bi
"hellomake" "libhellomake.dylib"  cdecl add-library
>>

LIBRARY: hellomake

FUNCTION: void myPrintHelloMake ( )