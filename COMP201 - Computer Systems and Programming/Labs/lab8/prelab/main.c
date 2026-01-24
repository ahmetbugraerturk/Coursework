#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 512
double startTime, stopTime;

double get_time_in_seconds() {
  struct timespec ts;
  clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &ts);
  return ts.tv_sec + ts.tv_nsec / 1e9;
}

/*  Sum all rows: */
void sumRows(int M[][n], int rowSums[]) {
  int i, j;

  for (i = 0; i < n; i++) {
    rowSums[i] = 0;
    for (j = 0; j < n; j++)
      rowSums[i] += M[i][j];
  }
}

/* Sum all columns: */
void sumColumns(int M[][n], int colSums[]) {
  int i, j;

  for (j = 0; j < n; j++) {
    colSums[j] = 0;
    for (i = 0; i < n; i++)
      colSums[j] += M[i][j];
  }
}

void rand_init(int M[][n]) {
  srand(time(NULL));
  int i, j;
  for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
      M[i][j] = (int)rand() % 256;
}

int main() {
  static int M[n][n];
  int rowSums[n];
  int colSums[n];

  rand_init(M);

  startTime = get_time_in_seconds();
  sumRows(M, rowSums);
  stopTime = get_time_in_seconds();
  printf("%d x %d Row Sum Takes %f secs\n", n, n, stopTime - startTime);

  startTime = get_time_in_seconds();
  sumColumns(M, colSums);
  stopTime = get_time_in_seconds();
  printf("%d x %d Column Sum Takes %f secs\n", n, n, stopTime - startTime);

  return 0;
}
