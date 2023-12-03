/*
 * Copy input.txt over to input1.txt
 * Run on input1.txt in Vim:
 * :0 put =line('$')
 * :%s/[a-z]//g
 */

#include <stdio.h>

int two_digit(int a) {
    int c = a % 10;

    while (a >= 10) {
        a /= 10;
    }

    return a * 10 + c;
}

int main() {
    FILE* f = fopen("input1.txt", "r");
    
    int sum = 0, num, T;

    fscanf(f, "%d", &T);
    printf("%d\n", T);

    while (T--) {
        fscanf(f, "%d", &num);
        sum += two_digit(num);
        printf("%d ", num);
    }

    printf("\n%d\n", sum);

    fclose(f);
}
