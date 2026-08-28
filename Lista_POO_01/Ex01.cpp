#include <iostream>
#include <cmath>
using namespace std;

class Circulo {
public:
    double raio;

    double area() {
        return M_PI * raio * raio;
    }
    double circunferencia() {
        return 2 * M_PI * raio;
    }
};

int main() {
    Circulo x;
    Circulo y;
    x.raio = 5;
    y.raio = 3;
    Circulo z=x;
    z.raio=20;
    cout << x.raio << " " << x.area() << " " << x.circunferencia() << endl;
    cout << y.raio << " " << y.area() << " " << y.circunferencia() << endl;
    return 0;
}
