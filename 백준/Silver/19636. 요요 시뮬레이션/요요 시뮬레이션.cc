#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int w, basic, t, day, d_input, d_output;

    // 입력
    cin >> w >> basic >> t;
    cin >> day >> d_input >> d_output;

    int w1 = w;
    int w2 = w;

    // 일일 기초대사량
    int basic2 = basic;

    for (int i=0; i<day; i++){
        w1 += d_input - (basic + d_output);
        w2 += d_input - (basic2 + d_output);
        // 기초대사량 변화 : w2에만 반영됨, 체중 변화 다음에 발생
        if (abs(d_input - (basic2 + d_output)) > t)
            basic2 += floor((d_input - (basic2+d_output))/2.0);
    }

    // 출력 01. 일일 기초대사량의 변화 반영 X
    if (w1 <= 0)
        cout << "Danger Diet\n";
    else
        cout << w1 << " " << basic << "\n";

    // 출력 02. 일일 기초대사량의 변화 반영 O
    if (w2 <= 0 || basic2 <= 0)
        cout << "Danger Diet\n";
    else{
        cout << w2 << " " << basic2 << " ";
        if (basic - basic2 > 0) // 체중이 아니라 일일 기초대사량으로 비교해야 함
            cout << "YOYO";
        else
            cout << "NO";
    }
}