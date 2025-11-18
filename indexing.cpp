#include<iostream>
#include<string>
using namespace std;

int main()
{
    string str;
    int i;
    char ch;
    bool found=false;

    cout<<"Enter any string : ";
    getline(cin,str);

    cout<<"Enter character to Search : ";
    cin >> ch ;
    cout<<endl;

    for(i=0;i<str.length();i++)
    {
        if(str[i]==ch)
        {
            cout<<"Character '"<< ch << "' found at index "<< i <<endl;
            found=true;
        }
    }
    if(!found)
    {
        cout<<"Character not found at string"<<endl;
    }
    return 0;
}
