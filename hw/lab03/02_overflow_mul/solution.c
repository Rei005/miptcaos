#include <stdio.h>
#include <limits.h>

int main(void) {
    int a = 0;
    int b = 0;

    if(scanf("%d %d", &a, &b) != 2) {
        return 1;
    }

    long long product = (long long)a * b;

    if ((product > 2147483647) || (product < -2147483648)) {
        printf("Overflow\n");
    } else {
        printf("Product: %lld\n", product);
    }
}