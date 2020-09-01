//https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=465
//prime ring problem uVA online judge

#include<bits/stdc++.h>

using namespace std;

bool isPrime(int n) 
{ 
    if (n <= 1)  return false; 
    if (n <= 3)  return true; 
    if (n%2 == 0 || n%3 == 0) return false; 
    for (int i=5; i*i<=n; i=i+6) 
        if (n%i == 0 || n%(i+2) == 0) 
           return false; 
    return true; 
} 

vector< int >vi;

void solve(int n,int i,int v[]){
    v[i]=1;
    vi.push_back(i+1);
    int j;
    for(j=0;j<n;j++){
        if(isPrime(j+1+vi.back()) && v[j]==0)
            solve(n,j,v);
    }
    if(vi.size()==n && isPrime(vi[0]+vi.back())){
        for(int k=0;k<vi.size()-1;k++)
        printf("%d ",vi[k]);
        printf("%d\n",vi.back());
    }
    if(j==n){
        v[i]=0;
        vi.pop_back();
    }
}

int main()
{
    int n,t=0;
    while(scanf("%d",&n)!=EOF){
        if(t>0)
        printf("\n");
        t++;
        printf("Case %d:\n",t);
        int v[16]={0}; 
        solve(n,0,v);
    }
}