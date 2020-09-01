#include<stdio.h>

int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        long long int x,y,a;
        scanf("%lld%lld",&x,&y);
        if(x>y){
            if(x%2==0)
            a=x*x-y+1;
            else
            a=(x-1)*(x-1)+y;
        }
        else{
            if(y%2==0)
            a=(y-1)*(y-1)+x;
            else
            a=y*y-x+1;
        }
        printf("%lld\n",a);
    }
    return 0;
}