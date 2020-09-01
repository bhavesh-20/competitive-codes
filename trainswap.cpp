#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n,i,j,cnt=0;
        scanf("%d",&n);
        int a[n];
        for(i=0;i<n;i++)
        scanf("%d",&a[i]);
        for(i=0;i<n;i++){
            for(j=i+1;j<n;j++){
                if(a[i]>a[j])
                cnt++;
            }
        }
        printf("Optimal train swapping takes %d swaps.\n",cnt);
    }
}