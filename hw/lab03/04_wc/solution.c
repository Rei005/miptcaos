#include <stdio.h>

int is_newline(int ch) {
    return ch == '\n';
}

int is_space(int ch) {
    return ch == ' ' || ch == '\t' || ch == '\n';
}

int main(void) {
    int ch;
    long lines = 0;
    long words = 0;
    long chars = 0;
    int in_word = 0;

    while ((ch = getchar()) != EOF) {
        chars++;

        if (is_newline(ch)) {
            lines++;
        }

        if (is_space(ch)) {
            in_word = 0;
        } else if (!in_word) {
            in_word = 1;
            words++;
        }
    }
    printf("Chars: %ld\n", chars);
    printf("Words: %ld\n", words);
    printf("Lines: %ld\n", lines);

    return 0;
}