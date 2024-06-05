#include <stdio.h>
#include <stdlib.h>

int f(int n, int a[]) {
    if (n < 1) 
        return 1 ;
    if (a[n] == 0) 
        a[n] = 2 * f(n - 1, a) + f(n - 2, a);
    printf("%d ", a[n]);
    return a[n] ;
}

int main() {
    int a[10] ;
    for (int i = 0; i < 10; i = i + 1){
        a[i] = 0 ;
    }
    printf("%d ",f(4, a)) ;
}
