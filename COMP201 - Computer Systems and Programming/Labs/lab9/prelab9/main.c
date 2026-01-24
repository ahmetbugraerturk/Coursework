#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define REPS 100

// ------------------------
// 1. LOOP UNROLLING
// ------------------------

int dot_product(int *vec1, int *vec2, int len) {
    int result = 0;
    for (int i = 0; i < len; i++) {
        result += vec1[i] * vec2[i];
    }
    return result;
}

int dot_product_optimized(int *vec1, int *vec2, int len) {
    // TODO: Implement 4-way loop unrolling for dot product
    int result = 0;
    int i=0;
    for (i = 0; i<len-4; i+=4){
    	result += vec1[i]*vec2[i];
	result += vec1[i+1]*vec2[i+1];
	result += vec1[i+2]*vec2[i+2];
	result += vec1[i+3]*vec2[i+3];
    }
    for (;i<len;i++){
    	result += vec1[i]*vec2[i];
    }

    return result;
}

// ------------------------
// 2. INLINING (via #define)
// ------------------------

int eval_poly(int x) {
    return (2 * x * x - 7 * x + 3);
}

#define EVAL_POLY(x) (2 * (x) * (x) - 7 * (x) + 3) // TODO: Replace (x) with the inlined polynomial expression

int sum_poly(int *arr, int len) {
    int sum = 0;
    for (int i = 0; i < len; i++) {
        sum += eval_poly(arr[i]);
    }
    return sum;
}

int sum_poly_inlined(int *arr, int len) {
    int sum = 0;
    // TODO: Use the EVAL_POLY macro instead of calling eval_poly()
    for (int i = 0; i<len; i++){
    	sum += EVAL_POLY(arr[i]);
    }

    return sum;
}

// ------------------------
// 3. CODE MOTION
// ------------------------

int count_vowels(char *str) {
    int count = 0;
    char vowels[] = "aeiouAEIOU";
    for (int i = 0; i < strlen(str); i++) {
        for (int j = 0; j < strlen(vowels); j++) {
            if (str[i] == vowels[j]) {
                count++;
                break;
            }
        }
    }
    return count;
}

int count_vowels_optimized(char *str) {
    // TODO: Optimize by moving loop-invariant computations outside the loop
    int count = 0;
    char vowels[] = "aeiouAEIOU";
    int vlen = 10;
    int slen = strlen(str);
    for (int i = 0; i<slen; i++){
	    for (int j = 0; j<vlen; j++){
		    if (str[i] == vowels[j]) {
			    count++;
			    break;
		    }
	    }
    }


    return count;
}

// ------------------------
// UTILITY: HIGH-RES TIMER
// ------------------------

double get_time_diff(struct timespec start, struct timespec end) {
    return (double)(end.tv_sec - start.tv_sec) +
           (double)(end.tv_nsec - start.tv_nsec) / 1e9;
}

// ------------------------
// UTILITY: TASK EVALUATION
// ------------------------

// Returns: 1 = passed, 2 = results mismatch, 3 = unoptimized faster
int evaluate_task(int result_unopt, int result_opt, double time_unopt, double time_opt) {
    if (result_unopt != result_opt) {
        return 2;
    } else if (time_opt >= time_unopt) {
        return 3;
    } else {
        return 1;
    }
}

void print_task_status(int task_num, const char *task_name, int status) {
    printf("Task %d (%s): ", task_num, task_name);
    if (status == 1) {
        printf("PASSED\n");
    } else if (status == 2) {
        printf("The results do not match, please correct your implementation.\n");
    } else {
        printf("Unoptimized code is faster, please ensure you optimized your code correctly.\n");
    }
}

void print_speedup(double time_unopt, double time_opt) {
    if (time_opt < time_unopt) {
        double speedup = time_unopt / time_opt;
        printf("Speedup: %.2fx\n\n", speedup);
    } else {
        printf("No speedup achieved.\n\n");
    }
}


// ------------------------
// MAIN FUNCTION
// ------------------------

int main(void) {
    int n = 100002;
    int *arr = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) arr[i] = i % 10;

    // Create a test string for Task 3
    int str_len = 4000;
    char *test_str = malloc(str_len + 1);
    for (int i = 0; i < str_len; i++) {
        test_str[i] = 'a' + (i % 26);  // Repeating lowercase letters
    }
    test_str[str_len] = '\0';

    struct timespec t1, t2;
    int result_unopt, result_opt;
    double time_unopt, time_opt;

    int task1_status = 0, task2_status = 0, task3_status = 0;

    // 1. dot_product vs optimized (Loop Unrolling)
    printf("Task 1 (Loop Unrolling - Dot Product):\n");
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_unopt = dot_product(arr, arr, n);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_unopt = get_time_diff(t1, t2) * 1e6;
    
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_opt = dot_product_optimized(arr, arr, n);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_opt = get_time_diff(t1, t2) * 1e6;
    printf("dot_product result: %d\n", result_unopt);
    printf("dot_product_optimized result: %d\n", result_opt);
    printf("Time (dot_product): %.2f microseconds\n", time_unopt);
    printf("Time (dot_product_optimized): %.2f microseconds\n", time_opt);
    print_speedup(time_unopt, time_opt);

    task1_status = evaluate_task(result_unopt, result_opt, time_unopt, time_opt);

    // 2. eval_poly vs macro inlined (Inlining)
    printf("Task 2 (Inlining):\n");
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_unopt = sum_poly(arr, n);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_unopt = get_time_diff(t1, t2) * 1e6;
    
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_opt = sum_poly_inlined(arr, n);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_opt = get_time_diff(t1, t2) * 1e6;
    printf("sum_poly result: %d\n", result_unopt);
    printf("sum_poly_inlined result: %d\n", result_opt);
    printf("Time (sum_poly): %.2f microseconds\n", time_unopt);
    printf("Time (sum_poly_inlined): %.2f microseconds\n", time_opt);
    print_speedup(time_unopt, time_opt);

    task2_status = evaluate_task(result_unopt, result_opt, time_unopt, time_opt);

    // 3. count_vowels vs optimized (Code Motion)
    printf("Task 3 (Code Motion - Count Vowels):\n");
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_unopt = count_vowels(test_str);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_unopt = get_time_diff(t1, t2) * 1e6;
    
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_opt = count_vowels_optimized(test_str);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_opt = get_time_diff(t1, t2) * 1e6;
    printf("count_vowels result: %d\n", result_unopt);
    printf("count_vowels_optimized result: %d\n", result_opt);
    printf("Time (count_vowels): %.2f microseconds\n", time_unopt);
    printf("Time (count_vowels_optimized): %.2f microseconds\n", time_opt);
    print_speedup(time_unopt, time_opt);

    task3_status = evaluate_task(result_unopt, result_opt, time_unopt, time_opt);

    printf("========== SUMMARY ==========\n");
    print_task_status(1, "Loop Unrolling", task1_status);
    print_task_status(2, "Inlining", task2_status);
    print_task_status(3, "Code Motion", task3_status);

    free(arr);
    free(test_str);
    return 0;
}
