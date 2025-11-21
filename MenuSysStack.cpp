#include<bits/stdc++.h>
using namespace std;

class Stack
    {
    public:
        vector<int>x;

        void push(int value)
        {
            x.push_back(value);
        }

        void pop()
        {
            if(x.size()>0) x.pop_back();
            else cout<<"Stack is empty\n";
        }

        void top()
        {
            if(x.size()>0) cout<<"Top Element : "<<x.back()<<endl;
            else cout<<"Stack is empty\n";
        }
        bool empty()
        {
            return x.size()==0;
        }
        int size()
        {
            return x.size();
        }

        void insert(int index,int value)
        {
            if(index<0 || index>x.size())
            {
                cout<<"Inavlid Index\n";
                return;
            }
            x.insert(x.begin()+index,value);
            cout<<"Inserted...!\n";
        }

        void deleteat(int index)
        {
            if(index<0 || index>=x.size())
            {
                cout<<"Invalid Index !\n";
                return ;
            }
            x.erase(x.begin()+index);
            cout<<"Deleted......!\n";
        }
        void show()
        {
            if(x.empty())
            {
                cout<<"Stack is empty\n";
                return;
            }
            cout<<"Stack element : ";
            for(int v:x) cout<<v<<" ";
            cout<<endl;
        }
    };

    int main()
    {
        Stack s;
        int ch;

        while(ch)
        {
            cout<<"\n-----MENU-----\n";
            cout<<"1. Push\n";
            cout<<"2. Pop\n";
            cout<<"3. Top Show\n";
            cout<<"4. Insert Element\n";
            cout<<"5. Delete Element\n";
            cout<<"6. Show All Element\n";
            cout<<"7. Size Element\n";
            cout<<"8. Exit\n";
            cout<<"Enter your choice : ";
            cin>>ch;

            if(ch==1)
            {
                int v;
                cout<<"Enter Value : ";
                cin>>v;
                s.push(v);
            }
            else if(ch==2)
            {
                s.pop();
            }
            else if(ch==3)
            {
                s.top();
            }
            else if(ch==4)
            {
                int index,value;
                cout<<"Enter index : ";
                cin>>index;
                cout<<"Enter Value : ";
                cin>>value;
                s.insert(index,value);
            }
            else if(ch==5)
            {
                int index;
                cout<<"Enter index : ";
                cin>>index;
                s.deleteat(index);
            }
            else if(ch==6)
            {
                s.show();
            }
            else if(ch==7)
            {
                cout<<"Element Size : "<<s.size();
            }
            else if(ch==8)
            {
                cout<<"Exiting...!\n";
                break;
            }
            else
            {
                cout<<"Invalid Choice..!\n";
            }
        }
        return 0;
    }
