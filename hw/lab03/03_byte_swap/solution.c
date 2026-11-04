#include <stdio.h>
#include <stdint.h>

uint32_t reverseBytes(uint32_t num) {
    return ((num >> 24) & 0x000000FF) |
           ((num >> 8)  & 0x0000FF00) |
           ((num << 8)  & 0x00FF0000) |
           ((num << 24) & 0xFF000000);
}

int main(void) {
    uint32_t input = 0;

    if (scanf("%u", &input) != 1) {
        return 1;
    }

    uint32_t result = reverseBytes(input);

    printf("Decimal: %u\n", result);
    printf("Hex: 0x%08X\n", result);

    return 0;
}