//https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3836

#include<bits/stdc++.h>

using namespace std;

int main(){
    int t,_t;
    scanf("%d",&t);
    for(_t=1;_t<=t;_t++){
        int n;
        scanf("%d",&n);
        char s[n+1],i;
        scanf("%s",s);
        int dot_count=0,cnt=0;
        for(i=0;s[i]!='\0';i++){
            if(s[i]=='.'){
                dot_count++;
            }
            else if(i-1>=0 && s[i]=='#' && s[i-1]=='.' && s[i+1]=='.' && dot_count%3!=0){
                dot_count++;
            }
            else{
                cnt=cnt + dot_count/3;
                if(dot_count%3!=0) cnt++;
                dot_count=0;
            }
        }
        cnt=cnt+dot_count/3;
        cnt=cnt+ (dot_count%3?1:0) ;
        printf("Case %d: %d\n",_t,cnt);
    }
    return 0;
}