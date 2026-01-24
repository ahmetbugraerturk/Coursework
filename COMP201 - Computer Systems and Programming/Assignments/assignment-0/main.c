#include <stdio.h>   // printf, scanf
#include <stdlib.h>  // malloc, free
#include "mylibrary.h"
#include "myprogram.h"

int main()
{
    int task, res;
    fprintf(stderr, "Which task to run? (1-5) ");
    scanf("%d", &task);

    if (task < 1 || task > 5)
    {
        fprintf(stderr, "Invalid task number.\n");
        return -1;
    }
    fprintf(stderr, "Task %d selected.\n", task);

    if (task == 1)
    {
        // sum_of_squares
        // Prompt for a single integer n, output 1^2 + 2^2 + ... + n^2
        fprintf(stderr, "Enter the number: ");
        scanf("%d", &res);         // reusing 'res' just to read user input
        int answer = sum_of_squares(res);
        printf("%d\n", answer);
    }
    else if (task == 2)
    {
        // product_of_positives
        // Prompt for how many numbers, read them into array, output product of all positive elements
        fprintf(stderr, "How many numbers? ");
        scanf("%d", &res);
        int count = res;
        int *a = (int *)malloc(sizeof(int) * count);
        if (!a) {
            fprintf(stderr, "Memory allocation failed.\n");
            return -1;
        }

        for (int i = 0; i < count; ++i)
            scanf("%d", &a[i]);

        int answer = product_of_positives(a, count);
        printf("%d\n", answer);

        free(a);
    }
    else if (task == 3)
    {
        // second_largest
        // Prompt for how many numbers, read them, output the second-largest distinct value
        fprintf(stderr, "How many numbers? ");
        scanf("%d", &res);
        int count = res;
        int *a = (int *)malloc(sizeof(int) * count);
        if (!a) {
            fprintf(stderr, "Memory allocation failed.\n");
            return -1;
        }

        for (int i = 0; i < count; ++i)
            scanf("%d", &a[i]);

        int answer = second_largest(a, count);
        printf("%d\n", answer);

        free(a);
    }
    else if (task == 4)
    {
        // sum_of_digits
        // Prompt for a single integer, output the sum of its digits
        fprintf(stderr, "Enter the number: ");
        scanf("%d", &res);
        int answer = sum_of_digits(res);
        printf("%d\n", answer);
    }
    else if (task == 5)
    {
        // lowercase_alphabet_index
        // Prompt for an index, output 'a' + index if 0 <= index < 26, else space
        fprintf(stderr, "Enter the index: ");
        scanf("%d", &res);
        char letter = lowercase_alphabet_index(res);
        printf("%c\n", letter);
    }

    // If your "wrapper()" function does something special, keep it here:
    wrapper();

    return 0;
}
