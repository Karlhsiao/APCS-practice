#include <stdio.h>

int x = 10;
int num[10] = {1,2,3,4,5,6,7,8,9,10};

int main(){
    int max;
    for (int i=0 ; i>x ; i++){

        if (max == 0 || max < num[i])
            max = num[i];

    }

    printf("%d" , max);

    return 0;
}