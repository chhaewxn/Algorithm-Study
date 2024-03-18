#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int countSimilarWords(const vector<string>& words) {
    int count = 0;

    multiset<char> baseSet(words[0].begin(), words[0].end()); // 첫 번째 단어의 문자로 이루어진 multiset 생성

    for (int i = 1; i < words.size(); ++i) {
        multiset<char> currentSet(words[i].begin(), words[i].end()); // i번째 단어의 문자로 이루어진 multiset 생성

        multiset<char> diffSet1, diffSet2; // 두 단어 간의 차집합을 담을 multiset
        set_difference(baseSet.begin(), baseSet.end(), currentSet.begin(), currentSet.end(), inserter(diffSet1, diffSet1.begin()));
        set_difference(currentSet.begin(), currentSet.end(), baseSet.begin(), baseSet.end(), inserter(diffSet2, diffSet2.begin()));

        // 두 단어 간의 차집합의 크기가 1 이하여야 비슷한 단어로 판별
        if (diffSet1.size() <= 1 && diffSet2.size() <= 1) {
            ++count;
        }
    }

    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<string> words(N);
    for (int i = 0; i < N; ++i) {
        cin >> words[i];
    }

    int similarWords = countSimilarWords(words); // 비슷한 단어 개수 계산

    cout << similarWords << '\n';

    return 0;
}
