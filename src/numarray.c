#include <stddef.h>
#include <stdlib.h>
#include <numarray.h>

// allocates memory for a numarray
int* numarray_alloc(size_t size) {
    return (int*) malloc(size * sizeof(int));
}

// frees memory for a numarray
void numarray_free(int* arr) {
    free(arr);
}

// gets the value of a numarray at index i
int numarray_get(int* arr, size_t i) {
    return arr[i];
}

// sets the value of a numarray at index i to val
void numarray_set(int* arr, size_t i, int val) {
    arr[i] = val;
}

// creates a numarray where the value at each index is that index
int* numarray_arange(size_t size) {
    int* arr = numarray_alloc(size);

    int i;
    for (i = 0; i < size; ++i) {
        arr[i] = i;
    }

    return arr;
}

// creates a numarray where each value is val
int* numarray_init(size_t size, int val) {
    int* arr = numarray_alloc(size);

    int i;
    for (i = 0; i < size; ++i) {
        arr[i] = val;
    }

    return arr;
}

// adds two numarrays of the same size
int* numarray_add(int* arr1, int* arr2, size_t size) {
    int* sum = numarray_alloc(size);

    int i;
    for (i = 0; i < size; ++i) {
        sum[i] = arr1[i] + arr2[i];
    }

    return sum;
}

// finds the difference of two numarrays of the same size
int* numarray_subtract(int* arr1, int* arr2, size_t size) {
    int* diff = numarray_alloc(size);

    int i;
    for (i = 0; i < size; ++i) {
        diff[i] = arr1[i] - arr2[i];
    }

    return diff;
}

// multiplies each value of a numarray by n
int* numarray_scalarmult(int* arr, int n, size_t size) {
    int* mult = numarray_alloc(size);

    int i;
    for (i = 0; i < size; ++i) {
        mult[i] = arr[i] * n;
    }

    return mult;
}

// Finds the dot product of two numarrays of the same size
int numarray_dot(int* arr1, int* arr2, size_t size) {
    int i;
    int sum = 0;
    for (i = 0; i < size; ++i) {
        sum += arr1[i] * arr2[i];
    }

    return sum;
}

void do_nothing() {
    // pass
}
