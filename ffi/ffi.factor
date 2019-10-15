USING: alien alien.c-types alien.libraries alien.syntax ;
IN: numerical-scratch.ffi

<< "numarray" "libnumarray.dylib"  cdecl add-library >>

LIBRARY: numarray

FUNCTION: int* numarray_alloc ( size_t size )

FUNCTION: void numarray_free ( int* arr )

FUNCTION: int numarray_get ( int* arr, size_t i )

FUNCTION: void numarray_set ( int* arr, size_t i, int val )

FUNCTION: int* numarray_arange ( size_t size )