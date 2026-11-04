#include <stdio.h>

int main(void) {
    unsigned long long addr = 0;
    unsigned long long align = 0;

    if (scanf("%llu %llu", &addr, &align) != 2 || align == 0) {
        return 1;
    }

    unsigned long long rem = addr % align;
    unsigned long long down = addr - rem;
    unsigned long long up = (rem == 0) ? addr : (down + align);

    if (rem == 0) {
        printf("Aligned: yes\n");
    } else {
        printf("Aligned: no\n");
    }

    printf("Down: %llu\n", down);
    printf("Up: %llu\n", up);

    return 0;
}