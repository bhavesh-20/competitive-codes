#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n,i;
        scanf("%d",&n);    
        int a[n],j;
        for(i=0;i<n;i++)
        scanf("%d",&a[i]);
        int sum=0;
        for(i=1;i<n;i++)
        {
            int cnt=0;
            for(j=i-1;j>=0;j--)
            {
                if(a[j]<=a[i])
                cnt++;
            }
            sum+=cnt;
        }
        printf("%d\n",sum);
    }
}