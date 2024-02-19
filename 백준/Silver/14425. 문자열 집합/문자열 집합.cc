#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int main() {

    int n, m;
    cin >> n >> m;

    unordered_set<string> strings;

    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        strings.insert(str);  // unordered_set에 문자열 추가
    }

    int count = 0;
    for (int i = 0; i < m; i++) {
        string str;
        cin >> str;

        if (strings.find(str) != strings.end()) {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
