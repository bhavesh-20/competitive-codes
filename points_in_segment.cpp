#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,m,x,y;
    cin>>n>>m;
    int i;
    vector< int >v,a(m+1,0);
    while(n--){
        cin>>x>>y;
        a[x-1]+=1;
        a[y]-=1;
    }
    for(i=1;i<m;i++){
        a[i]+=a[i-1];
    }

    for(i=0;i<m;i++){
        if(a[i]<=0)
        v.push_back(i+1);
    }
    cout<<v.size()<<"\n";
    for(i=0;i<v.size();i++)
    cout<<v.at(i)<<" ";
}