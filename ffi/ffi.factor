USING: alien alien.c-types alien.libraries alien.syntax ;
IN: numerical-scratch.ffi

<< "numarray" "libnumarray.dylib"  cdecl add-library >>

LIBRARY: numarray

FUNCTION: int* new_numarray ( size_t size )

FUNCTION: int numarray_get ( int* arr, size_t i )

FUNCTION: void numarray_set ( int* arr, size_t i, int val )