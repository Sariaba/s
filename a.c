#include <stdio.h>

void PrintWelcome() {
    printf("Welcome to the second program!\n");
}

void PrintOdd(int num, int start) {
    int counter = 0;
    int currentNumber = start;

    printf("The first %d odd numbers starting from %d are: ", num, start);

    while (counter < num) {
        if (currentNumber % 2 != 0) {
            printf("%d", currentNumber);
            counter++;

            if (counter < num) {
                printf(",");
            }
        }
        currentNumber--;
    }

    printf("\n");
}

int main() {
    PrintWelcome();

    int num, start;
    printf("Please enter a negative integer: ");
    scanf("%d", &num);

    printf("Please enter the start value: ");
    scanf("%d", &start);

    PrintOdd(num, start);

    return 0;
}
