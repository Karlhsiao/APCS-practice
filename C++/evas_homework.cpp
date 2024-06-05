#include <iostream>

using namespace std;

int main(){
    int times;
    int a, b, c, d;

    cin >> times;

    for (int i = 0; i <= times; i++){
        cin >> a >> b >> c >> d;

        if (d - c == c - b && c - b == b - a){
            cout << a << " " << b << " " << c << " " << d << " " << d + ( c - b ) << endl;
        } else {
            cout << a << " " << b << " " << c << " " << d << " " << d * ( c / b ) << endl;
        }

    }
}