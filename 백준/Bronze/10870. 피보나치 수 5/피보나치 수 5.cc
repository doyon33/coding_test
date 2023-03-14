#include <iostream>
#include <array>
using namespace std;

int main() {
    int input, result, fn_1, fn_2; 
    array<int, 21> fibonacci;
    fibonacci[0] = 0;
    fibonacci[1] = 1;

    cin >> input;
    for (int i = 2; i < input+1; i++) {
        fibonacci[i] = fibonacci[i-2] + fibonacci[i-1];
    }
    cout << fibonacci.at(input);
    return 0;
}