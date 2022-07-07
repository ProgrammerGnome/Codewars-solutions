This my first solution:
```C
#include <stdio.h>

int main() {
  int arr[] = { 4, 3, 9, 7, 2, 5 };
  int n = sizeof(arr) / sizeof(int);

  printf("Array: ");
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }

  int min1;
  int min2;

  min1 = arr[0];
  int index = 0;
  for (int i = 1; i < n; i++) {
    if (arr[i] < min1)
      min1 = arr[i];
    index = i;
  }

  int pos = index;
  int size = 6;
  for (int i = pos - 1; i < size - 1; i++) {
    arr[i] = arr[i + 1];
  }

  min2 = arr[0];
  for (int i = 1; i < n; i++) {
    if (arr[i] < min2)
      min2 = arr[i];
  }

  printf("\nThe sum of the two lowest positive numbers: ");
  printf("%d\n", min1 + min2);

  return 0;
}
```
This my second solution:
```C
#include <stdio.h>

void swap(int* xp, int* yp)
{
  int temp = *xp;
  *xp = *yp;
  *yp = temp;
}

// A function to implement bubble sort
void bubbleSort(int arr[], int n)
{
  int i, j;
  for (i = 0; i < n - 1; i++)

    // Last i elements are already in place
    for (j = 0; j < n - i - 1; j++)
      if (arr[j] > arr[j + 1])
        swap(&arr[j], &arr[j + 1]);
}

/* Function to print an array */
void printArray(int arr[], int size)
{
  int i;
  for (i = 0; i < size; i++)
    printf("%d ", arr[i]);
  printf("\n");
}

// Driver program to test above functions
int main()
{
  int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
  int n = sizeof(arr) / sizeof(arr[0]);
  printf("Array: "); printArray(arr, n);
  bubbleSort(arr, n);
  printf("The sum of the two lowest positive numbers: ");
  printf("%d\n",arr[0]+arr[1]);
  return 0;
}
```
