USING: alien alien.c-types alien.libraries alien.syntax ;
IN: numerical-scratch.ffi

<< "numarray" "/Users/nandeekanayak/Documents/College/Senior Year/Fall 2019/CS 183/numerical-scratch/lib/libnumarray.dylib"  cdecl add-library >>

LIBRARY: numarray

FUNCTION: int* numarray_alloc ( size_t size )

FUNCTION: void numarray_free ( int* arr )

FUNCTION: int numarray_get ( int* arr, size_t i )

FUNCTION: void numarray_set ( int* arr, size_t i, int val )

FUNCTION: int* numarray_arange ( size_t size )

FUNCTION: int* numarray_init ( size_t size, int val )

FUNCTION: int* numarray_add ( int* arr1, int* arr2, size_t size )

FUNCTION: int* numarray_subtract ( int* arr1, int* arr2, size_t size )

FUNCTION: int* numarray_scalarmult ( int* arr, int n, size_t size )

FUNCTION: int numarray_dot ( int* arr1, int* arr2, size_t size )

FUNCTION: void do_nothing ( )