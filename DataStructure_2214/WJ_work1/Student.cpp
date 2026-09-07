#include <iostream>
#include "Student.h"
using namespace std;
Student::Student() {
    ID = "";
    fname = "";
    lname = "";
    nname = "";
    tel = "";
    gmail = "";
}

void Student::addID(string newID) {
    ID = newID;
}
void Student::addName(string newFname, string newLname) {
    fname = newFname;
    lname = newLname;
}
void Student::addNickName(string newNname) {
    nname = newNname;
}
void Student::addTel(string newTel) {
    tel = newTel;
}
void Student::addEmail(string newGmail) {
    gmail = newGmail;
}

void Student::showData() {
    cout << "ID: " << ID << endl;
    cout << "First Name: " << fname << endl;
    cout << "Last Name: " << lname << endl;
    cout << "Nickname: " << nname << endl;
    cout << "Telephone: " << tel << endl;
    cout << "Email: " << gmail << endl;
}
