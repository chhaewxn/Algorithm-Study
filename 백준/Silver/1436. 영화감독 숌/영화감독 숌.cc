#include <iostream>
#include <string>

using namespace std;

const int SIX_SIX_SIX = 666;

string getTitle(int order) {
    int currentNumber = 665;  // 666이 영화 제목에 사용된 경우도 있기에 665부터 시작
    while (order > 0) {
        currentNumber++;

        // 현재 숫자에 666이 포함되어 있으면 order를 감소시킴
        if (to_string(currentNumber).find("666") != string::npos) {
            order--;
        }
    }

    // 찾은 숫자를 문자열로 변환하여 반환
    return to_string(currentNumber);
}

int main() {
    // 찾을 영화 순서 입력
    int order;
    cin >> order;

    // 주어진 순서의 '666'을 포함하는 영화 제목 구하기
    string movieTitle = getTitle(order);

    // 결과 출력
    cout << movieTitle << '\n';

    return 0;
}
