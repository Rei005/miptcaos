#include <gtest/gtest.h>
#include "calc.h"

TEST(MathLibTest, Addition) {
    EXPECT_EQ(add(2, 3), 5);
    EXPECT_EQ(add(-1, 1), 0);
}

TEST(MathLibTest, Subtraction) {
    EXPECT_EQ(sub(5, 3), 2);
    EXPECT_EQ(sub(0, 5), -5);
}

TEST(MathLibTest, Multiplication) {
    EXPECT_EQ(multiply(3, 4), 12);
    EXPECT_EQ(multiply(-2, 3), -6);
}
