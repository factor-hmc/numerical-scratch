USING: kernel locals math math.vectors numerical-scratch.ffi tools.time ;
IN: numerical-scratch.benchmark

<PRIVATE

! Given a size, create the numarrays for benchmarking
:: create_numarrays ( n -- a1 a2 )
! Create the array [0, 1, 2, ...]
n numarray_arange
! Create the array [4, 4, 4, ...]
n 4 numarray_init ;

! Actually run the benchmarking for adding
:: benchmark_numarray_add ( a1 a2 n #t -- time )
! Benchmark
[ #t [ a1 a2 n numarray_add numarray_free ] times ] benchmark
! Compute the average
#t / >float
;

! Actually run the benchmarking for dot product
:: benchmark_numarray_dot ( a1 a2 n #t -- time )
! Benchmark
[ #t [ a1 a2 n numarray_dot drop ] times ] benchmark
! Compute the average
#t / >float
;

! Given a size, create the vectors for benchmarking
:: create_vectors ( n -- v1 v2 )
! Create the vector [0, 1, 2, ...]
0 n 1 - [a,b]
! Create the vector [4, 4, 4, ...]
n 4 numarray_init ;


PRIVATE>

! Given an numarray size, and number of trials, benchmark adding and dot product
:: benchmark_numarray ( n #t -- add dot )
! Create the arrays
n create_numarrays :> a2 :> a1
! Benchmark
a1 a2 n #t benchmark_numarray_add
a1 a2 n #t benchmark_numarray_dot
! Free the arrays
a1 numarray_free a2 numarray_free ;