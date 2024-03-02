#include <iostream>
#include <vector>

using namespace std;

void luckyWheel(int N, int K) {
    vector<char> wheel(N, '?');
    auto iter = wheel.begin();

    for (int i = 0; i < K; ++i) {
        int S;
        char C;
        cin >> S >> C;
        S %= N;

        for (int j = 0; j < S; ++j) {
            if (iter == wheel.begin())
                iter = wheel.end() - 1;
            else
                --iter;
        }

        if (*iter == '?')
            *iter = C;
        else if (*iter != C) {
            cout << "!\n";
            return;
        }
    }

    for (auto outer = wheel.begin(); outer != wheel.end(); ++outer) {
        for (auto inner = wheel.begin(); inner != wheel.end(); ++inner) {
            if (*outer == *inner && outer != inner && *inner != '?') {
                cout << "!\n";
                return;
            }
        }
    }

    for (int i = 0; i < N; ++i) {
        if (iter == wheel.end())
            iter = wheel.begin();
        cout << *iter;
        ++iter;
    }

    cout << "\n";
}

int main() {
    int N, K;
    cin >> N >> K;

    luckyWheel(N, K);

    return 0;
}
