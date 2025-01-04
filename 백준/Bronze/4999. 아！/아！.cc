#include <iostream>
#include <string>
using namespace std;

int count(string st) {
    int len = st.length();
    int cnt = 0;
    for (int i=0; i<len-1; i++){
        if (st[i] == 'a'){cnt ++;}
    }
    return cnt;
}

int main() {
    string a = "";
    string b = "";
    cin >> a;
    cin >> b;
    int a_cnt=count(a), b_cnt=count(b);
    if(a_cnt >= b_cnt){cout<<"go";}
    else{cout<<"no";}
    
    return 0;
}