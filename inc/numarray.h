/*
 * Test numerical array properties
 */

#include <stddef.h>


int* numarray_alloc(size_t size);

void numarray_free(int* arr);

int numarray_get(int* arr, size_t i);

void numarray_set(int* arr, size_t i, int val);

int* numarray_arange(size_t size);

int* numarray_add(int* arr1, int* arr2, size_t size);

void do_nothing();