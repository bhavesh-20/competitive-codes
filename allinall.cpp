//https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1281

#include<bits/stdc++.h>

using namespace std;

int main(){
    char s1[100000],s2[10000000];
    while(scanf("%s%s",s1,s2)!=EOF){ 
    int i,j=0;
    int m=0;
    for(i=0;s1[i]!='\0';i++);
    m=i;
    for(i=0;s2[i]!='\0';i++){
        if(s2[i]==s1[j]) j++;
        if(j==m) break;
    }
    if(j==m)printf("Yes\n");
    else printf("No\n");
    }
}
//using true cpp....above code is written in c.
/*
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    string s;
    while(getline(cin,s))
    {
        string w,s1,s2;
        stringstream iss(s);
        while(iss>>w){
            if(s1=="")
            s1=w;
            else
            s2=w;
        }
        int j=0;
        for(int i=0;i<s2.size();i++)
        {
            if(s2[i]==s1[j])
            {
                j++;
            }
        }
        if(j==s1.size())
        {
            cout<<"Yes"<<endl;
        }
        if(j!=s1.size())
        {
            cout<<"No"<<endl;
        }
    }
    return 0;
}
*/