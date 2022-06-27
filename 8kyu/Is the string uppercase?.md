Create a method to see whether the string is ALL CAPS.

Examples (input -> output)
```
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
```
In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is 
trivially considered to be in ALL CAPS.

```C
#include <stdio.h>
#include <string.h>

int main(void) {

  int max;
  printf("Enter a length of string: ");
  scanf("%d", & max);
  char string[max];
  printf("Enter a string: ");
  scanf("%s", & string);

  int upper = 0;
  int lower = 0;

  for (int i = 0; i < max; i++) {
    if (string[i] > 64 && string[i] < 91) {
      upper++;
    }
    if (string[i] > 96 && string[i] < 123) {
      lower++;
    }
  }

  if (max == upper) {
    printf("True");
  } else {
    printf("False");
  }

  return 0;
}
```
