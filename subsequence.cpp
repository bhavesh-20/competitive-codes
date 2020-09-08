//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3562
#include<bits/stdc++.h>

using namespace std;

int main(){
    long long int n,s;
    while(scanf("%lld%lld",&n,&s)!=EOF){
        long long int a[n];
        long long int i,sum=0,mi=100000000000000,start=0;
        for(i=0;i<n;i++) cin>>a[i];
        
        for(i=0;i<n;i++){
            sum+=a[i];
            while(sum>=s && start<=i){
                mi=(mi<(i-start+1)?mi:(i-start+1));
                sum-=a[start];
                start++;
            }   
        }
        if(mi==100000000000000)
        mi=0;
        printf("%lld\n",mi);
    }
    return 0;
}