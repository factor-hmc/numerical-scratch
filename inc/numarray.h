/*
 * Test numerical array properties
 */

#include <stddef.h>


int* new_numarray(size_t size);

int numarray_get(int* arr, size_t i);

void numarray_set(int* arr, size_t i, int val);