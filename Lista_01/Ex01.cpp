#include <iostream> //input e output

using namespace std;

int main() { //chaves == tab em python
    cout << "Digite seu nome: "; //enviando texto para a saída (<<)
    string nome; //declaração de variável -- sequência não importa
    cin >> nome;
    cout << "Olá, " << nome << endl;
    return 0;
}

//Como compilar um arquivo c++
//g++ "nome do arquivo".cpp -o "nome do arquivo"