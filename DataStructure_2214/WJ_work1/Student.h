#ifndef Student_h
#define Student_h
#include <string>

class Student {
private:
    std::string ID;
    std::string fname;
    std::string lname;
    std::string nname;
    std::string tel;
    std::string gmail;
public:
    Student();
    void addID(std::string newID);
    void addName(std::string newFname, std::string newLname);
    void addNickName(std::string newNname);
    void addTel(std::string newTel);
    void addEmail(std::string newGmail);
    void showData();
};
#endif