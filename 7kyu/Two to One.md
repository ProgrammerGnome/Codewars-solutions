Take 2 strings s1 and s2 including only letters from a to z. 
Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
```
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```
This my solution:
```C
#include <stdio.h>
#include <string.h>

void swap(int * xp, int * yp) {
  int temp = * xp;
  * xp = * yp;
  * yp = temp;
}

// A function to implement bubble sort
void bubbleSort(int arr[], int n) {
  int i, j;
  for (i = 0; i < n - 1; i++)

    // Last i elements are already in place
    for (j = 0; j < n - i - 1; j++)
      if (arr[j] > arr[j + 1])
        swap( & arr[j], & arr[j + 1]);
}

/* Function to print an array */
void printArray(int arr[], int size) {
  int i;
  for (i = 0; i < size; i++)
    printf("%d ", arr[i]);
  printf("\n");
}

// Sort Driver and Main code 
int main() {
  //Main code
  int max;
  int max_2;

  printf("Enter a length of 1. string: ");
  scanf("%d", & max);

  printf("Enter a length of 2. string: ");
  scanf("%d", & max_2);

  char string[max];
  char string_2[max_2];

  printf("Enter a 1. string: ");
  scanf("%s", & string);

  printf("Enter a 2. string: ");
  scanf("%s", & string_2);

  strcat(string, string_2);

  int arr[max + max_2] = {};

  for (int i = 0; i < sizeof(string) + sizeof(string_2); i++) {
    char myChar = string[i];
    for (int i = 0; i < sizeof(string) + sizeof(string_2); ++i) {
      if (string[i] > 64 && string[i] < 91) {
        arr[i] = string[i];
      } else if (string[i] > 96 && string[i] < 123) {
        arr[i] = string[i];
      } else {
        continue;
      }
    }
    break;
  }
  printf("\n");

  char mystr[sizeof(string) + sizeof(string_2)];
  for (int i = 0; i < sizeof(string) + sizeof(string_2); i++) {
    if (arr[i] > 64 && arr[i] < 123) {
    } else {
      continue;
    }
  }

  //Bubble sort driver
  int n = sizeof(arr) / sizeof(arr[0]);
  bubbleSort(arr, n);

  //Remove Duplicate Elements
  int i, j, k;
  for (i = 0; i < max + max_2; i++) {
    for (j = i + 1; j < max + max_2; j++) {
      if (arr[i] == arr[j]) {
        for (k = j; k < max + max_2 - 1; k++) {
          arr[k] = arr[k + 1];
        }
        max + max_2--;
        j--;
      }
    }
  }

  //Print arr[] to char
  printf("A new sorted string: ");
  for (i = 0; i < max + max_2; i++) {
    printf("%c", arr[i]);
  }

  printf("\n");
  return 0;
}
```
