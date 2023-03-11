#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int count = 0;

    cin >> s;
    for (string::iterator it = s.begin() + 1; it < s.end(); ++it) {
        if (*it != *(it - 1)) {
            ++count;
        }
    }
    if (count % 2 == 0) {
        cout << count / 2;
    }
    else
        cout << (count+1) / 2; // 2;
    
}
