//http://codeforces.com/problemset/problem/706/B

#include<bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin>>n;
    int max=0,i;
    int a[n];
    for(i=0;i<n;i++){
        cin>>a[i];
        max = max>a[i]?max:a[i];
    }
    int b[max];
    sort(a,a+n);
    int j=0;
    int cnt=0;
    for(i=0;i<max;i++){
        while(i+1==a[j]){
            j++;
            cnt++;
        } 
        b[i]=cnt;
    }
    int p,x;
    scanf("%d",&p);
    while(p--){
        scanf("%d",&x);
        if(x>max) printf("%d\n",n);
        else printf("%d\n",b[x-1]);
    }
    return 0;
}

