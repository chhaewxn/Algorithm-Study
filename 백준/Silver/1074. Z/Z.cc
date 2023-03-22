#include <stdio.h>
#include <math.h>

int Z(int N, int r, int c) {
    if (N == 0) return 0;

    int Square = (int)pow(2, N);
    int nextSquare = Square / 2;

    if (r < nextSquare && c < nextSquare) { // 1사분면
        return Z(N - 1, r, c);
    }
    else if (r < nextSquare && c >= nextSquare) { // 2사분면
        return nextSquare * nextSquare + Z(N - 1, r, c - nextSquare);
    }
    else if (r >= nextSquare && c < nextSquare) { // 3사분면
        return nextSquare * nextSquare * 2 + Z(N - 1, r - nextSquare, c);
    }
    else {  // 4사분면
        return nextSquare * nextSquare * 3 + Z(N - 1, r - nextSquare, c - nextSquare);
    }
}


int main() {
    int N, r, c;
    scanf("%d %d %d", &N, &r, &c);

    int count = Z(N, r, c);
    printf("%d\n", count);

    return 0;
}