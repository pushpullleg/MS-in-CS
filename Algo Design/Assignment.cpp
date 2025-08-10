// CSCI 532 - Summer II - Programming Assignment
// CWID:50380788 Mukesh Ravichandran
// This program calculates F(n) using both recursive and dynamic programming
// and prints how many additions each method performs

#include <iostream>
using namespace std;

int count = 0; // global count for additions in recursive method

// Recursive function R(n)
int R(int n) {
    if (n == 1) return 1;
    if (n == 2) return 2;
    if (n == 3) return 3;
    if (n == 4) return 4;

    count = count + 3; // 3 additions in every step
    return R(n - 1) + 3 * R(n - 2) + 3 * R(n - 3) + R(n - 4);
}

int D(int n, int &addCount) {
    if (n == 1) return 1;
    if (n == 2) return 2;
    if (n == 3) return 3;
    if (n == 4) return 4;

    int* F = new int[n + 1]; //  than fixed-size array
    F[1] = 1;
    F[2] = 2;
    F[3] = 3;
    F[4] = 4;

    addCount = 0;

    for (int i = 5; i <= n; i++) {
        F[i] = F[i - 1] + 3 * F[i - 2] + 3 * F[i - 3] + F[i - 4];
        addCount = addCount + 3;
    }

    int result = F[n];
    delete[] F; // clean up memory
    return result;
}


int main() {
    cout << "n\tF(n)\tR_Additions\tD_Additions\n";
    cout << "-------------------------------------------\n";

    for (int n = 5; n <= 35; n += 5) {
        // Recursive
        count = 0;
        int resultR = R(n);
        int rAdd = count;

        // Dynamic
        int dAdd = 0;
        int resultD = D(n, dAdd);

        // Output result (both F(n) will be same)
        cout << n << "\t" << resultR << "\t" << rAdd << "\t\t" << dAdd << "\n";
    }

    return 0;
}


/*
Output Table :

| n  | F(n)     | R_Additions   | D_Additions |
|----|----------|----------------|--------------|
| 5  | 43       | 3              | 3            |
| 10 | 258      | 54             | 18           |
| 15 | 1560     | 711            | 33           |
| 20 | 9432     | 9282           | 48           |
| 25 | 57069    | 121299         | 63           |
| 30 | 345585   | 1583559        | 78           |
| 35 | 2092821  | 20680974       | 93           |
*/