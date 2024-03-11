#include <stdio.h>
#include <stdlib.h>
//  return a dynamically allocated C-string
//  this output will be freed by the tester

char *number_to_string(int number) {
    char *str = (char *)malloc(11 * sizeof(char));

    if (str == NULL) { return NULL; }

    sprintf(str, "%d", number);

    return str;
}


