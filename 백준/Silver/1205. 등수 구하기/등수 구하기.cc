#include<stdio.h>

int main()
{
	int N, my_score, P; // N은 현재 랭킹 리스트에 있는 점수, my_score은 내 점수, P는 랭킹 리스트에 들어갈 수 있는 점수 개수
	int score[50]; // 랭킹 리스트 

	int rankcount = 0;  // 등수 카운트
	int my_rank = 1; // 내 등수

	scanf("%d %d %d", &N, &my_score, &P);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &score[i]); // 현재 랭킹 리스트에 있는 점수 N개 입력받기
	}

	for (int i = 0; i < N; i++)
	{
		if (my_score < score[i])
		{
			my_rank++; // 내 점수가 랭킹 리스트에 있는 점수 미만의 값이면 내 등수 +1
		}
		else if (my_score == score[i])
		{} // 이 부분 놓쳐서 오래걸림 .. 
		else break; // 같거나 작으면 break;
		rankcount++; // 랭킹 리스트에서 내 점수보다 높은 점수의 총 개수 count
	}

	//예외
	if (rankcount == P) // 내 점수보다 높은 점수의 개수가 P와 같으면 랭킹리스트에 못올라가므로
	{
		my_rank = -1; // 랭킹리스트에 올라갈 수 없으므로 -1 출력
	}

	//답 출력
	printf("%d\n", my_rank);
	return 0;
}