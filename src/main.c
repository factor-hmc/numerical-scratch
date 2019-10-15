#include <stdio.h>
#include <numarray.h>

int main() {
    // Create a new array
    int* arr = new_numarray(2);

    // Populate the array so that it looks like [10, 3]
    numarray_set(arr, 0, 10);
    numarray_set(arr, 1, 3);

    // Print the result
    printf("[%d, %d]\n", numarray_get(arr, 0), numarray_get(arr, 1));

    return 0;
}