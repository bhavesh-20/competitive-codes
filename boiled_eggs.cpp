//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3051

#include<bits/stdc++.h>

using namespace std;

int main(){
    int t,n,p,q;
    scanf("%d",&t);
    for(int _t=1;_t<=t;_t++){
        scanf("%d%d%d",&n,&p,&q);
        int i,a[n];
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
        }
        int cnt=0;
        for(i=0;i<n;i++){
            if(a[i]>q || p==0) break;
            cnt++;
            q=q-a[i];
            p--;
        }
        printf("Case %d: %d\n",_t,cnt);
    }
    return 0;
}