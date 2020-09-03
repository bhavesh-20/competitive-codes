//http://codeforces.com/contest/230/problem/A
#include<bits/stdc++.h>

using namespace std;

bool custom_sort(const pair<int,int> &a,const pair<int,int> &b){
    if(a.first!=b.first) return a.first<b.first;
    else return a.second>b.second;
}

int main(){
    int z,p,x,y;
    scanf("%d%d",&z,&p);
    int f=0,n=p;
    vector< pair< int,int> >v;
    while(p--){
        scanf("%d%d",&x,&y);
        v.push_back(make_pair(x,y));
    }
    sort(v.begin(),v.end(),custom_sort);
    for(int i=0;i<v.size();i++){
        x=v[i].first;
        y=v[i].second;
        if(z>x) z+=y;
        else{
            f=1;
            break;
        }
    }
    if(f==1)printf("NO\n");
    else printf("YES\n");
    return 0;
}