/* Exercise 6: Types Of Variables */

#include <stdio.h>

int main()
{
    int distance = 100;
    float power = 2.456f;
    double super_power = 56789.4532;
    char initial = 'A';
    char first_name[] = "Zed";
    char last_name[] = "Shaw";

    printf("Distance %d ... \n", distance);
    printf("Power %f ... \n", power);
    printf("Super_power %f ... \n", super_power);
    printf("Initial %c ... \n", initial);
    printf("First_name %s ... \n", first_name);
    printf("Last_name %s ... \n", last_name);

    return 0;
}   