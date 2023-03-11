#include <iostream>
using namespace std;

int main() {
    int num;

    cin >> num;
    for (int i = 1; i < num+1; i++) { //num = 5 : *
        for (int space = num-i; space > 0; space--) {
            cout << " ";
        }
        for (int star = 1; star < i+1; star++) {
            cout << "* ";
        }
        cout << "\n";
    }
}