#include <stdio.h>
#include <numarray.h>

int main() {
    // Create a new array
    int* arr = numarray_alloc(2);

    // Populate the array so that it looks like [10, 3]
    numarray_set(arr, 0, 10);
    numarray_set(arr, 1, 3);

    // Print the result
    printf("[%d, %d]\n", numarray_get(arr, 0), numarray_get(arr, 1));

    // Free this array
    numarray_free(arr);

    // Create the array [0, 1, 2, 3, 4] and print it
    arr = numarray_arange(5);
    printf("[%d, %d, %d, %d, %d]\n", arr[0], arr[1], arr[2], arr[3], arr[4]);

    // Free this array
    numarray_free(arr);

    return 0;
}