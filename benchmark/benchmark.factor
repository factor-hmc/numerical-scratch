USING: alien.c-types alien.data kernel locals math math.ranges math.vectors
numerical-scratch.ffi sequences specialized-arrays.instances.alien.c-types.int
tools.time typed ;
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
#t / >float ;

! Actually run the benchmarking for dot product
:: benchmark_numarray_dot ( a1 a2 n #t -- time )
! Benchmark
[ #t [ a1 a2 n numarray_dot drop ] times ] benchmark
! Compute the average
#t / >float ;

! Given a size, create the vectors for benchmarking
:: create_vectors ( n -- v1 v2 )
! Create the vector [0, 1, 2, ...]
0 n 1 - [a,b] int >c-array
! Create the vector [4, 4, 4, ...]
0 n 1 - [a,b] [ drop 4 ] map int >c-array ;

! Actually run the benchmarking for adding
TYPED:: benchmark_vector_add ( a1: int-array a2: int-array n #t -- time )
! Benchmark
0 [ #t [ a1 a2 v+ length + ] times ] benchmark
swap drop
! Compute the average
#t / >float ;

! Actually run the benchmarking for dot product
TYPED:: benchmark_vector_dot ( a1: int-array a2: int-array n #t -- time )
! Benchmark
0 [ #t [ a1 a2 v. + ] times ] benchmark
swap drop
! Compute the average
#t / >float ;

PRIVATE>

! Given a numarray size, and number of trials, benchmark adding and dot product
:: benchmark_numarray ( n #t -- l1 add l2 dot )
! Create the arrays
n create_numarrays :> a2 :> a1
! Benchmark
"Adding numarrays"
a1 a2 n #t benchmark_numarray_add
"Dot producting numarrays"
a1 a2 n #t benchmark_numarray_dot
! Free the arrays
a1 numarray_free a2 numarray_free ;

! Given a vector size, and number of trials, benchmark adding and dot product
:: benchmark_vector ( n #t -- l1 add l2 dot )
! Create the arrays
n create_vectors :> a2 :> a1
! Benchmark
"Adding vectors"
a1 a2 n #t benchmark_vector_add
"Dot producting vectors"
a1 a2 n #t benchmark_vector_dot ;