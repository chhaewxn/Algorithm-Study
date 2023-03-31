#include <stdio.h>

int paper[2500][2500];
int count[3];

void divide(int x, int y, int size) {
    int i, j, k, flag = 1, first = paper[x][y];
    for (i = x; i < x+size && flag; i++) {
        for (j = y; j < y+size && flag; j++) {
            if (paper[i][j] != first) {
                flag = 0;
                break;
            }
        }
    }
    if (flag) {
        count[first+1]++;
    } else {
        int s = size / 3;
        for (i = x; i < x+size; i += s) {
            for (j = y; j < y+size; j += s) {
                divide(i, j, s);
            }
        }
    }
}

int main() {
    int n, i, j;
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &paper[i][j]);
        }
    }
    divide(0, 0, n);
    for (i = 0; i < 3; i++) {
        printf("%d\n", count[i]);
    }
    return 0;
}