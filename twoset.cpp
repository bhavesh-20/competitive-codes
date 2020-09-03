#include<bits/stdc++.h>

using namespace std;

void print(const vector< int > &v1,const vector< int > &v2){
    printf("%d\n",v1.size());
    for(int i=0;i<v1.size();i++) printf("%d ",v1.at(i));
    printf("\n");
    printf("%d\n",v2.size());
    for(int i=0;i<v2.size();i++) printf("%d ",v2.at(i));
}

int main(){
    int n,z=0;
    scanf("%d",&n);
    vector< int >v1,v2;
    if(n%4==0){
        printf("YES\n");
        for(int i=1;i<=n/2;i++){
            if(z==0){
                z=1;
                v1.push_back(i);
                v1.push_back(n-i+1);
            }
            else{
                z=0;
                v2.push_back(i);
                v2.push_back(n-i+1);
            }
        }
        print(v1,v2);
    }
    else if(n%4==3){
        printf("YES\n");
        v1.push_back(1);
        v1.push_back(2);
        v2.push_back(3);
        if(n>3)
        for(int i=4;i<=4+(n-4)/2;i++){
            if(z==0){
                z=1;
                v1.push_back(i);
                v1.push_back(n-i+4);
            }
            else{
                z=0;
                v2.push_back(i);
                v2.push_back(n-i+4);
            }
        }
        print(v1,v2);
    }
    else printf("NO\n");
}