//https://school.programmers.co.kr/learn/courses/30/lessons/70129

#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

vector<int> solution(string s) {
    string str = s;
    
    int loop_count = 0;       //반복 횟수
    int num_zero = 0;         //0의 개수
    string binary_str = "";   //이진 변환 후 str으로 저장할 변수
        
    vector<int> answer;      //리턴 값 미리 선언

    while (str != "1")    //문제 조건이 1이 될 때까지 반복이므로
    {
        string temp = "";   //0을 삭제한 후의 str을 담을 변수
        int str_size = str.size(); 
        
        for (int i = 0; i < str_size; i++)
        {
            if (str[i] == '0') //string을 한자리씩 검사하여 0을 찾으면
            {
                num_zero++;    //0의 개수를 카운트하고
            } 
            else               //0이 아니라면
            {
                temp.append("1"); //결과 str에 1을 추가
            }
        }
        int a = temp.size();      //0을 삭제한 결과 str의 길이
        
        vector<int> binary_temp = {}; //이진 변환을 하나씩 한 결과값을 담을 배열(역순)
        int x = a;  //처음 나눌 수(1차 결과 str의 길이)
        int q;      //몫을 담을 변수
        do
        {//이진 변환 알고리즘
            q = x / 2;
            int r = x - q*2;
            x = q;
            binary_temp.push_back(r);
        }
        while (q != 0);

		//이진 변환 결과 배열의 요소를 뒤에서부터 차례로 연결하는 for문
        for (int i = binary_temp.size() - 1; i > -1 ; i--)
        {
            string y = to_string(binary_temp[i]);
            binary_str.append(y);
        }
        str = binary_str;    //결과값을 다시 str에 저장(다음 loop를 위한 값)
        binary_temp.clear(); //변수 초기화
        binary_str = "";     //변수 초기화
        loop_count ++;       //반복 횟수 카운트
    }
    answer.push_back(loop_count);
    answer.push_back(num_zero);

    return answer;
}
