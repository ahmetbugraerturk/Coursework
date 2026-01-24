#include <stdio.h>


// Name: Ahmet Buğra Ertürk
// Student Id: 0086877
// Date: 11.12.2025
// Honor Code: I declare hereby that I have completed this assignment with honesty and integrity.






int f1(int x, int y) {
	int s = x + y;
	int m = x * y;
	if (s>m) {
		return s;
	}
	return m;
}


int f2(int arr[], int n) {
	long x = 0;
	while (n>x){
		if(arr[x]<-5) return arr[x];
		x++;
	}
	return arr[0];
	
}



int main(){

   if (f1(2,2) == 4 && f1(6,10) == 60 && f1(1,2) == 3){
	   printf("f1 test passed! \n");
   }
   else{
     printf("f1 test failed:( \n");
   }
   
    int arr1[] = {-5, 4 ,0, -1, 2};
    int arr2[] = {1, 2, 3, 4, 5};
    int arr3[] = {0, -10, -9, -8, -7, -6};
    int arr4[] = {[0]=-4, [1]=3, [2]=4,[3]=-6, [4]=-7};    

    if (f2(arr1, 5) == -5 && f2(arr2, 5) == 1 && f2(arr3, 6) == -10 && f2(arr4,5)==-6){
      printf("f2 test passed! \n");
    }
    else{
      printf("f2 test failed:( \n");
    }
   return 0;
}
