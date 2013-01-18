/*
1_6_3 | "The Trip"
Authors:
  Steven
  Alex
  Zack
  Daniel
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  do {
    int num_of_students;
    int *student_costs; // initializing student cost array
    int total_cost = 0;
    int average_cost = 0;
    int num_over_avg = 0;
    int total_over_avg = 0;
    int extra_cents = 0;
    int answer;
    int i;

    scanf("%i\n", &num_of_students); // grab number of students

    if (num_of_students == 0) {
      break;
    }

    student_costs = malloc(num_of_students * sizeof(int)); // allocating memory to array

    for (i=0; i<num_of_students; i++) {
      int dollars, cents;
      scanf("%d.%d\n", &dollars, &cents);
      student_costs[i] = dollars * 100 + cents;
      total_cost += student_costs[i];
    }

    average_cost = total_cost / num_of_students;

    for (i=0; i<num_of_students; i++) {
      int amount_over = student_costs[i] - average_cost;
      if (amount_over > 0) {
        num_over_avg++;
        total_over_avg += amount_over;
      }
    }

    extra_cents = total_cost % num_of_students;

    answer = total_over_avg - ((extra_cents < num_over_avg) ? extra_cents : num_over_avg);

    printf("$%d.%02d\n", answer / 100, answer % 100);

    free(student_costs);
  } while (1);
}