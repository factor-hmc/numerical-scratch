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

    // Create two arrays [0, 1, 2] and [2, 2, 2] and add them
    size_t size = 3;
    int* arr1 = numarray_arange(size);
    int* arr2 = numarray_alloc(size);

    int i;
    for (i = 0; i < size; ++i) {
        arr2[i] = 2;
    }

    // Add the arrays and print the result
    arr = numarray_add(arr1, arr2, size);
    printf("[%d, %d, %d]\n", arr[0], arr[1], arr[2]);

    numarray_free(arr);

    // Now try taking the dot product
    int sum = numarray_dot(arr1, arr2, size);
    printf("dot([0, 1, 2], [2, 2, 2]) = %d\n", sum);

    numarray_free(arr1);
    numarray_free(arr2);

    return 0;
}