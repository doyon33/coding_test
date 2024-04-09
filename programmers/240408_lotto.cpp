#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int returnRank(int num) //return ranks of lotto
{
    if (num < 2) {return 6;}       //hit nums < 2, rank 6th
    else if (num == 2) {return 5;} //hit nums = 2, rank 5th
    else if (num == 3) {return 4;} //hit nums = 3, rank 4th
    else if (num == 4) {return 3;} //hit nums = 4, rank 3rd
    else if (num == 5) {return 2;} //hit nums = 5, rank 2nd
    else if (num == 6) {return 1;} //hit nums = 6, rank 1st
    else
    {
        cout << "input number is over 6";
        return 0;
    }
};

vector<int> solution(vector<int> lottos, vector<int> win_nums)
{
    vector<int> answer;  //return value
    int numOfZero = 0;   //number of 0 in lottos
    int min = 0;    //minimum number of hit numbers
    int max = 0;    //maximum number of hit numbers

    for (int elem:lottos)
    {
      //if there's same number in win_nums(which means one number of lottos hit)
        if (find(begin(win_nums), end(win_nums), elem) != end(win_nums))
        {
          //count as hit number
            min++;
            max++;
        }
        else if (elem == 0) //count number of 0
        {
            numOfZero ++;
        }
    }

    max += numOfZero;

    answer = {returnRank(max), returnRank(min)}; //change hit numbers to its ranks

    return answer;
};

int main(void) { //test case
    vector<int> input1{44, 1, 0, 0, 31, 25};
    vector<int> input2{31, 10, 45, 1, 6, 19};
    vector<int> a = solution(input1, input2);
    for(int&i : a)
    {
        cout << i << " ";
    }
};
