#include<bits/stdc++.h>

using namespace std;

void swap(int *p,int *q){
    int temp=*p;
    *p=*q;
    *q=temp;
}


int main(){
    int n;
    scanf("%d",&n);
    int a[n],i;
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    if(n==1)
    printf("%d",a[0]);
    else{
        for(i=1;i<n;i++)
        {
            if(i%2==1)
            {
                if(a[i]<a[i-1])
                swap(&a[i],&a[i-1]);
            }
            else{
                if(a[i]>a[i-1])
                swap(&a[i],&a[i-1]);
            }
        }
        for(i=0;i<n;i++)
        printf("%d ",a[i]);
    }
}