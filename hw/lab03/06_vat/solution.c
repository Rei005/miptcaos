#include <stdio.h>

int main(void) {
    unsigned long long price = 0;
    if (scanf("%llu", &price) != 1) {
        return 1;
    }

    unsigned long long quotient = price * 2 / 10;
    unsigned long long remainder = price * 2 % 10;

    unsigned long long vat = quotient;
    if (remainder >= 5) {
        vat += 1;
    }

    unsigned long long total = price + vat;

    printf("VAT: %llu\n", vat);
    printf("Total: %llu\n", total);

    return 0;
}