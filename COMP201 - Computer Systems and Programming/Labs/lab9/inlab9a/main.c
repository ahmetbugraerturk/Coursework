#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define REPS 10

// ------------------------
// 1. LOOP UNROLLING - Even Column Sum
// ------------------------

int even_col_sum(int **mat, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j += 2) {
            sum += mat[i][j];
        }
    }
    return sum;
}

int even_col_sum_optimized(int **mat, int size) {
    // TODO: Implement 4-way loop unrolling for even column sum
    // Hint: Make sure to handle remaining elements when the size is not divisible by 8.
    
    int sum = 0;
    for (int i = 0; i<size; i++){
    	int j = 0;
	for (; j<size-8; j+=8){
		sum+=mat[i][j];
		sum+=mat[i][j+2];
		sum+=mat[i][j+4];
		sum+=mat[i][j+6];
	}
	for (; j<size; j+=2){
		sum+=mat[i][j];
	}
    }
    
    return sum;
}

// ------------------------
// 2. INLINING (via #define)
// ------------------------

int scale_shift(int x, int shift) {
    return (x * 3 + shift) % 11;
}

#define SCALE_SHIFT(x, s) ((x)*3 + s)%11 // TODO

int mat_scale_sum(int **mat, int size, int shift) {
    int sum = 0;
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            sum += scale_shift(mat[i][j], shift);
    return sum;
}

int mat_scale_sum_inlined(int **mat, int size, int shift) {
    int sum = 0;
    // TODO: Use the SCALE_SHIFT macro instead of calling scale_shift()
    for (int i = 0; i<size; i++){
    	for (int j = 0; j<size; j++){
		sum += SCALE_SHIFT(mat[i][j], shift);
	}
    }

    return sum;
}
// ------------------------
// 3. CODE MOTION - Border Sum
// ------------------------

int border_sum(int **mat, int size) {
    int sum = 0;
    // Top and bottom rows
    for (int j = 0; j < size; j++) {
        sum += mat[0][j];
        sum += mat[size-1][j];
    }
    // Left and right columns (excluding corners)
    for (int i = 1; i < size - 1; i++) {
        sum += mat[i][0];
        sum += mat[i][size-1];
    }
    return sum;
}

int border_sum_optimized(int **mat, int size) {
    // TODO: Optimize by caching pointers and hoisting loop-invariant computations
    // Hint: There is 1 loop invariant arithmetic operation and 2 pointer dereferences worth caching (plus one more with
    // tiny impact in the second loop, you can skip that one if you want).
    int sum = 0;
    int l_idx = size-1;
    int* temp1 = mat[0];
    int* temp2 = mat[l_idx];
    for (int j = 0; j<size; j++){
    	sum+=temp1[j];
    	sum+=temp2[j];
    }
    for (int i = 1; i<l_idx; i++){
    	int* mati = mat[i];
	sum+=mati[0];
	sum+=mati[l_idx];
    }
    
    return sum;
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
    int size = 1004;
    int shift = 7;

    // Allocate matrix
    int **mat = malloc(sizeof(int*) * size);
    for (int i = 0; i < size; i++) {
        mat[i] = malloc(sizeof(int) * size);
        for (int j = 0; j < size; j++) {
            mat[i][j] = (i + j) % 5;
        }
    }

    struct timespec t1, t2;
    int result_unopt, result_opt;
    double time_unopt, time_opt;

    int task1_status = 0, task2_status = 0, task3_status = 0;

    // 1. even_col_sum vs optimized (Loop Unrolling)
    printf("Task 1 (Loop Unrolling - Even Column Sum):\n");
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_unopt = even_col_sum(mat, size);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_unopt = get_time_diff(t1, t2) * 1e6;
    
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_opt = even_col_sum_optimized(mat, size);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_opt = get_time_diff(t1, t2) * 1e6;
    printf("even_col_sum result: %d\n", result_unopt);
    printf("even_col_sum_optimized result: %d\n", result_opt);
    printf("Time (even_col_sum): %.2f microseconds\n", time_unopt);
    printf("Time (even_col_sum_optimized): %.2f microseconds\n", time_opt);
    print_speedup(time_unopt, time_opt);

    task1_status = evaluate_task(result_unopt, result_opt, time_unopt, time_opt);

    // 2. mat_scale_sum vs macro inlined (Inlining)
    printf("Task 2 (Inlining - Matrix Scale Shift Sum):\n");
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_unopt = mat_scale_sum(mat, size, shift);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_unopt = get_time_diff(t1, t2) * 1e6;
    
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_opt = mat_scale_sum_inlined(mat, size, shift);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_opt = get_time_diff(t1, t2) * 1e6;
    printf("mat_scale_sum result: %d\n", result_unopt);
    printf("mat_scale_sum_inlined result: %d\n", result_opt);
    printf("Time (mat_scale_sum): %.2f microseconds\n", time_unopt);
    printf("Time (mat_scale_sum_inlined): %.2f microseconds\n", time_opt);
    print_speedup(time_unopt, time_opt);

    task2_status = evaluate_task(result_unopt, result_opt, time_unopt, time_opt);

    // 3. border_sum vs optimized (Code Motion)
    printf("Task 3 (Code Motion - Border Sum):\n");
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_unopt = border_sum(mat, size);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_unopt = get_time_diff(t1, t2) * 1e6;
    
    clock_gettime(CLOCK_MONOTONIC, &t1);
    for (int i = 0; i < REPS; i++) result_opt = border_sum_optimized(mat, size);
    clock_gettime(CLOCK_MONOTONIC, &t2);
    time_opt = get_time_diff(t1, t2) * 1e6;
    printf("border_sum result: %d\n", result_unopt);
    printf("border_sum_optimized result: %d\n", result_opt);
    printf("Time (border_sum): %.2f microseconds\n", time_unopt);
    printf("Time (border_sum_optimized): %.2f microseconds\n", time_opt);
    print_speedup(time_unopt, time_opt);

    task3_status = evaluate_task(result_unopt, result_opt, time_unopt, time_opt);

    printf("========== SUMMARY ==========\n");
    print_task_status(1, "Loop Unrolling", task1_status);
    print_task_status(2, "Inlining", task2_status);
    print_task_status(3, "Code Motion", task3_status);

    // Free matrix
    for (int i = 0; i < size; i++) {
        free(mat[i]);
    }
    free(mat);
    
    return 0;
}
