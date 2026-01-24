#include "mylibrary.h"

int sum_of_squares(int n)
{
    int result = 0;
    // TODO: Calculate the sum of squares from 1 to n:
    //       1^2 + 2^2 + 3^2 + ... + n^2
    for (int i = 1; i<n+1;i++){ //iterate each number from 1 to n
	    result += i*i; //add the square of the number to "result" variable
    }
    return result;
}

int product_of_positives(int* array, int count)
{
    int product = 1;
    // TODO: Multiply only the strictly positive numbers (>0) in the array.
    //       Ignore or skip zeros and negative numbers.
    for (int i = 0; i<count; i++){ //itrate the array's indices
	    if (array[i]>0){ //check if the number is positive
		    product *= array[i]; //calculate the product
	    }
    }
    return product;
}

int second_largest(int* array, int count)
{
    // TODO: Find the second largest distinct value in the array.
    //       For example, if array = [1, 4, 2, 4, 5], the second largest is 4.
    //       Edge cases to ignore:
    //         - All elements are the same
    //         - Array size == 1
    int second = 0;
    int first = array[0];
    for (int i = 1; i<count ; i++){
	    if (array[i]>first){
		    second = first;
		    first = array[i];
	    }
	    else if (array[i]>second){
		    second = array[i];
	    }
    }
    return second;
}

int sum_of_digits(int number)
{
    int s = 0;
    // TODO: Sum all digits of 'number'.
    //       Example: if number = 1234, the result should be 10 (1+2+3+4).
    while (number > 0){
	    int r = number % 10;
	    s += r;
	    number = (number-r)/10;
    }
    return s;
}

char lowercase_alphabet_index(int index)
{
    // TODO: For index = 0, return 'a'. For index = 1, return 'b', up to index = 25 for 'z'.
    //       If index is out of [0..25], return a space ' '.
    char alph[] = "abcdefghijklmnopqrstuvwxyz";
    if (index >= 0 && index <26){
	    return alph[index];
    }
    return ' ';
}

