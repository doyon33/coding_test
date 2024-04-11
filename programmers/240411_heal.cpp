// https://school.programmers.co.kr/learn/courses/30/lessons/250137?language=cpp

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks)
{
    int current_health = health;
    int continuous = 0;
    int time = 0;
    int i = 0;
    
    while (time < attacks.back()[0]+1)
    {
        if (attacks[i][0] == time)
        {
            current_health -= attacks[i][1]; // 공격 데미지
            if (current_health < 1)
                return -1;
            continuous = 0;                //공격 당하면 연속 시간 초기화
            i++;
        }
        else
        {
            continuous ++;                //시전 시간 +1

            current_health += bandage[1];   //초당 회복량

            if (continuous == bandage[0]) {  //추가회복량 판정
                current_health += bandage[2];
                continuous = 0;
            }
            if (current_health > health) {  //최대 체력 확인
                current_health = health;
            }
        }
        time ++;
        
    }

    return current_health;
}
