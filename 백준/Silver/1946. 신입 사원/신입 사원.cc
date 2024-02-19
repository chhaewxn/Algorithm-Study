#include <iostream>
#include <vector>
#include <algorithm>

struct Applicant {
    int documentScore;
    int interviewScore;
};

bool compareByDocumentScore(const Applicant &a, const Applicant &b) {
    return a.documentScore < b.documentScore;
}

void hireApplicants(const std::vector<Applicant> &applicants) {
    int hired = 1; // 첫 번째 지원자는 무조건 합격
    int minInterviewScore = applicants[0].interviewScore;

    for (int i = 1; i < applicants.size(); ++i) {
        if (applicants[i].interviewScore < minInterviewScore) {
            minInterviewScore = applicants[i].interviewScore;
            hired++;
        }
    }

    std::cout << hired << "\n";
}

int main() {
    int testCases;
    std::cin >> testCases;

    while (testCases--) {
        int n;
        std::cin >> n;

        std::vector<Applicant> applicants(n);

        for (int i = 0; i < n; ++i) {
            std::cin >> applicants[i].documentScore >> applicants[i].interviewScore;
        }

        // 문서 성적을 기준으로 오름차순 정렬
        std::sort(applicants.begin(), applicants.end(), compareByDocumentScore);

        hireApplicants(applicants);
    }

    return 0;
}
