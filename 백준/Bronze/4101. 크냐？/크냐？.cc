#include <iostream>
using namespace std;

int main() {
    int a = 0;
    int b = 0;
    while (true) {
        cin >> a >> b;
        if (a == 0){
            break;
        }
        if (a > b) {
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }
    return 0;
}