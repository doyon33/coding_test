//https://school.programmers.co.kr/learn/courses/30/lessons/12951#

#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <iterator>
using namespace std;

string solution(string s)
{
    string answer = "";
    istringstream ss(s);
    string word = "";
    vector<string> s_list;
    s_list.clear();
    bool lastSpace = false;
    
    while(getline(ss, word, ' '))
        s_list.push_back(word); //string 리스트에 공백을 기준으로 나눈 문자열을 요소로 추가
    
    for (int i=0; i<s_list.size(); i++)
    {
        char ch[s_list[i].length()];   //임시 char 문자열을 만들어
        strcpy(ch, s_list[i].c_str()); //s_list의 요소 하나씩을 char로 변환
        
        if ((int)ch[0] > 96 and (int)ch[0] < 123) //97 ~ 122 소문자라면
            ch[0] -= 32;				 //대문자로 바꿔주고
        for (int j=1; j<s_list[i].length(); j++)
        {
            if ((int)ch[j] > 63 and (int)ch[j] < 92)//64 ~ 91 대문자라면
                ch[j] += 32;				//소문자로 바꿔준다
        }
        s_list[i] = (string)ch;
    }
    if (s.back() == ' ')
        lastSpace = true; //마지막에 공백이 있다
    stringstream ss2;
    for (auto it=s_list.begin(); it!=s_list.end(); it++)
    {
        if (it!=s_list.begin())
            ss2 << " ";
        ss2 << *it;
    }
    if (lastSpace)  //마지막에 공백이 있다면
        ss2 << " "; //추가
    answer = ss2.str(); //다시 스트링으로 바꿔주고
    return answer; //리턴
}
