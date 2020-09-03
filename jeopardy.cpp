//http://codeforces.com/problemset/problem/413/C
#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,m;
    long long int sum=0,x=0;
    cin>>n>>m;
    int a[n],b[m];
    vector< int >v;
    for(int i=0;i<n;i++){
        cin>>a[i];
        sum+=a[i];
    }
    long long int max=0;
    for(int i=0;i<m;i++){
        cin>>b[i];
        v.push_back(a[b[i]-1]);
        max= max>a[b[i]-1]?max:a[b[i]-1];
        sum-=a[b[i]-1];
    }
    if(sum>max) sum+=sum;
    else sum+=max;
    for(int i=0;i<m-1;i++)sum+=sum;
    printf("%lld\n",sum);
    return 0;
}