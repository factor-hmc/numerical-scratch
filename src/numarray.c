#include <stddef.h>
#include <stdlib.h>
#include <numarray.h>

int* new_numarray(size_t size) {
    return (int*) malloc(size);
}

int numarray_get(int* arr, size_t i) {
    return arr[i];
}

void numarray_set(int* arr, size_t i, int val) {
    arr[i] = val;
}