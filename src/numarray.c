#include <stddef.h>
#include <stdlib.h>
#include <numarray.h>

int* numarray_alloc(size_t size) {
    return (int*) malloc(size);
}

void numarray_free(int* arr) {
    free(arr);
}

int numarray_get(int* arr, size_t i) {
    return arr[i];
}

void numarray_set(int* arr, size_t i, int val) {
    arr[i] = val;
}

int* numarray_arange(size_t size) {
    int i;
    int* arr = numarray_alloc(size);

    for (i = 0; i < size; ++i) {
        arr[i] = i;
    }

    return arr;
}