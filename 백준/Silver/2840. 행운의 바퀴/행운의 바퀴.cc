#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<char> data(n, '?');
    int idx = 0;
    bool check = true;

    for (int i = 0; i < k; ++i) {
        int num;
        char alphabet;
        cin >> num >> alphabet;

        idx = (idx + num) % n;

        if (data[idx] != '?') {
            if (data[idx] == alphabet) {
                continue;
            }
            check = false;
        } else {
            data[idx] = alphabet;
        }
    }

    for (int i = 0; i < n; ++i) {
        if (data[i] == '?') {
            continue;
        }
        for (int j = i + 1; j < n; ++j) {
            if (data[i] == data[j]) {
                check = false;
                break;
            }
        }
    }

    if (check) {
        for (int i = 0; i < n; ++i) {
            cout << data[idx];
            idx = (idx - 1 + n) % n;
        }
    } else {
        cout << '!';
    }

    return 0;
}
