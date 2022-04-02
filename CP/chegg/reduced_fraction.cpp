// #include<bits/stdc++.h>

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int gcd(int x, int y); //prototype of working GCD function

int main(){
    if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}

    int num, denom;    //numerator and denominator, respectively
    char fmt;          // character to store 'f' or 'm'

    scanf("%d %d %c", &num, &denom, &fmt);

    float decimal = (float) num / denom;
    /*
        To get the reduced fraction we can divide numerator and denominator both with thier GCD.
        Because GCD stands for greatest common divisor of both numbers, SO after dividing it
        we get get numbers wihtout any common divisors except 1.

        For mixed number format:
            Let numerator = n,
            denominator = m,
            integer_part_of_division = w,
            and remainder_of_division = r
            then mixed number format is: w r/m
    */

    int gc = gcd(num, denom);     // division by GCD to get simple reduced form
    int reduced_num = num / gc;
    int reduced_denom = denom / gc;

    int whole_part = reduced_num / reduced_denom;  // whole part of reduced form (integer division)
    int fraction_part = reduced_num % reduced_denom;  // fractional part (remainder) of reduced form

    printf("Decimal: %.3f\n", decimal);

    if (decimal==(int)decimal){  // If result of division is integer then print nothing except decimal format
        return 0;
    }

    if (whole_part==0 or fmt=='f'){  // for zero whole part and fractional format
        printf("Reduced fracton: %d/%d\n", reduced_num, reduced_denom);
    }
    else{  // for mixed number format
        printf("Reduced mixed number: %d %d/%d\n", whole_part, fraction_part, reduced_denom);
    }
    return 0;
}

int gcd(int x, int y)
{
    while(y!=0){ int t = y;  y = x % y;  x = t; }
    return x;
}
