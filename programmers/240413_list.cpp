//https://school.programmers.co.kr/learn/courses/30/lessons/135808

#include <string>
#include <vector>
#include <algorithm> //sort()

using namespace std;

int solution(int k, int m, vector<int> score) {
    int answer = 0; // 정답(최대 이익)
    
    int max_box = (score.size() / m) * m; //반복 횟수(정수) 계산
    sort(score.begin(), score.end(), greater<>()); //score 배열 내림차순 정렬
    
    for (int i = 0; i < max_box; i+=m)
    {
        for (int j = i; j < i+m; j++)
        {
            if (score[j] < k) //m개 요소 내에 현재 최고 점수보다 낮은 요소가 있으면
                k = score[j]; //최저 점수로 바꿔줌
        }
        answer += k * m; //점수 확정되면 개수m만큼 곱하여 answer에 더함
    }
    return answer;
}
