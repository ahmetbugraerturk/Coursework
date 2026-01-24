#include "puzzles.h"

int puzzle1(int num) {
    int a = 0;
    
    for (int i = 0; i<num; i+=3 ) { 
        if ((i&1)&(i&1)) { 
            a-=i;
        } else {
            a+=i;
        }
    }
    return a;
}

int puzzle2(int limit) {
    int b = 0;
    int k = 1;

    while (1) { 
        
        b = b+k+k; 
        
        if (k>=limit) {
            break;
        }
        
        k++;
    }
    return b;
}

int puzzle3(int *arr, int len) {
    int c = 0;
    int i = 0;
    
    do {
        int x = arr[i] ;
        
        if (x>10) {
            c++;
        }
        
        i++;
    } while (i<len); 
    
    return c;
}
