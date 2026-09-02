#include <iostream>
#include "Student.h"
#include <string>
using namespace std;

int main() {
    Student s1; 

    s1.addID("6751010981");
    s1.addName("Wassana", "Juajaroen");
    s1.addNickName("Maprang");
    s1.addTel("0916883830");
    s1.addEmail("maprang.prang.pam@gmail.com");

    cout << "--- Data Student ---" << endl;
    s1.showData();

    return 0;
}