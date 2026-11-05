#include <stdio.h>
#include <stdint.h>

int main(void) {
    int cmd = 0;
    uint8_t reg = 0;

    while(scanf("%d", &cmd) == 1) {
        if (cmd == 0) {
            break;
        } else if(cmd == 1) {
            uint8_t mov;
            if (scanf("%hhd", &mov) == 1) {
                reg |= (uint8_t)(1 << mov);
            }
        } else if (cmd == 2) {
            uint8_t mov;
            if (scanf("%hhd", &mov) == 1) {
                reg &= ~(1 << mov);
            }
        } else if (cmd == 3) {
            uint8_t mov;
            if (scanf("%hhd", &mov) == 1) {
                reg ^= (1 << mov);
            }
        } else if(cmd == 4) {
            for (int i = 7; i >= 0; i--) {
                printf("%hhd", (reg >> i) & 1);
            }
            printf("\n");
        }
    }

    return 0;
}