#include<bits/stdc++.h>
using namespace std;

class Student{
    public:
    string name;
    double* cgpaPtr;

    Student(string name,double cgpa){
        this->name = name;
        cgpaPtr = new double;
        *cgpaPtr = cgpa;
    }
// this is the shallow copy
    // Student(Student &obj){
    //     this->name = obj.name;
    //     this->cgpaPtr = obj.cgpaPtr;
    // }

    // this is the deep copy
    Student(Student &obj){
        this->name = obj.name;
        cgpaPtr = new double;
        *cgpaPtr = *obj.cgpaPtr;
    }

    void getInfo(){
        cout<< "name: "<< name << endl ;
        cout<< "cgpa:" << *cgpaPtr <<endl ;
    }
};

int main(){

    Student st("jakaria",8.9);

    Student s2(st);
    st.getInfo();
    *(s2.cgpaPtr) = 9.2;

    st.getInfo();


return 0;
}
