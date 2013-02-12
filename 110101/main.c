/*
 * Homework1.c
 *
 *  Created on: 2013-1-15
 *      Author: Tom
 *      Edited by: Steven, Alex, and Zack
 */

#include <stdio.h>
#include <assert.h>

static int COUNTER = 0;

void doWork(int, int); // prototype'd

int main(int argc, char **argv) {
  int m,n,r;
  // r = scanf("%i %i\n",&m,&n);
  // doWork(m,n);
  do {
    r = scanf("%i %i\n",&m,&n);
    if (r != EOF) {
      doWork(m,n);
      printf("\n");
    }
  } while (r != EOF);
  return 0;
}

long int generateNumber(long int i) {
  if (i == 1) {
    COUNTER++;
    return 0;
  } else if (i % 2 == 0) {
    COUNTER++;
    return generateNumber(i / 2);
  } else {
    COUNTER++;
    return generateNumber(i * 3 + 1);
  }
}

void doWork(int i, int j) {
  int temp = 0;
  int k = i;
  int max = j;
  if (j < i) {
    k = j;
    max = i;
  }
  for (; k <= max; k++) {
    COUNTER = 0;
    generateNumber(k);
    if (COUNTER > temp) {
      temp = COUNTER;
    }
  }
  printf("%i %i %i", i, j, temp);
}

