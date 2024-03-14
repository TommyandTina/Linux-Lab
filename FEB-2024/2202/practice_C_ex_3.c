#include <stdio.h>
#include <stdlib.h>
#include <string.h>


double add(double a, double b) { return a + b; }
double sub(double a, double b) { return a - b; }
double mul(double a, double b) { return a * b; }
double divide(double a, double b) { return a / b; }



int main() {
    double (*operation)(double, double);
    double n0, n1;
    char oper;
	
	printf("\nEnter operation:");
	scanf(" %c",&oper);
	printf("\nEnter n0:");
	scanf("%lf",&n0);
	printf("\nEnter n1:");
	scanf("%lf",&n1);	
	

    switch (oper) {
        case '+':
            operation = add;
            break;
        case '-':
            operation = sub;
            break;
        case '*':
            operation = mul;
            break;
        case '/':
            operation = divide;
            break;
        default:
            printf("Invalid operation\n");
            return 1;
    }

    printf("\nResult: %.2f\n", operation(n0, n1));

    return 0;
}

