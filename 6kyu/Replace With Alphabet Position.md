#### Replace With Alphabet Position

Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet. 
If anything in the text isn't a letter, ignore it and don't return it. "a" = 1, "b" = 2, etc. 
Example: alphabet_position("The sunset sets at twelve o' clock.") 
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STR(num) #num

int main(void) {

  int max;
  printf("Enter a length of string: ");
  scanf("%d", & max);
  char string[max];
  printf("Enter a string: ");
  scanf("%s", & string);

  char string2[] = "";

  for (int i = 0; i < sizeof(string); i++) {
    char myChar = string[i];
    //printf(STR(String: )": ");
    for (int i = 0; i < sizeof(string); ++i) {
      if (string[i] > 64 && string[i] < 91) {
        string2[i] = string[i] - 64;
        //printf("%d, ",string[i]-64);
      } else if (string[i] > 96 && string[i] < 123) {
        string2[i] = string[i] - 96;
        //printf("%d, ",string[i]-96);
      } else {
        continue;
      }
    }
    break;
  }
  printf("\b\b\n");

  char mystr[sizeof(string)];
  for (int i = 0; i < sizeof(string); i++) {
    if (string2[i] > 0 && string2[i] < 27) {
      sprintf(mystr, "%d", string2[i]);
      printf("%s ", mystr);
    } else {
      continue;
    }
  }

  exit(EXIT_SUCCESS);

  return 0;
}
```
