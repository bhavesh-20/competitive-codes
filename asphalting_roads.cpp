//http://codeforces.com/problemset/problem/583/A

#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,m,i,x,y;
    cin>>n;
    m=n*n;
    set< int >row;
    set< int >column;
    for(i=0;i<m;i++){
        cin>>x>>y;
        if(row.find(x)!=row.end() || column.find(y)!=column.end())continue;
        else{
            row.insert(x);
            column.insert(y);
            printf("%d ",i+1);
        } 
    }
    printf("\n");
    return 0;
}