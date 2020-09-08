//https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=2531
#include<iostream>
#include<cstdio>
#include<cstring>
#include<utility>
#include<set>
#include<queue>
using namespace std;
 
typedef long long int64;
typedef pair<int,int>pii;
 
const int INF = 0x3f3f3f3f;
const int MAXN = 1000010;
 
int n, m, k;
int arr[MAXN];
int cnt[MAXN];
 
void init(){
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 3;
    for(int i=4; i<=n; ++i)
        arr[i] = (arr[i-1]+arr[i-2]+arr[i-3])%m + 1;
	memset(cnt, 0, sizeof(cnt));
}
 
int main(){
    int nCase, cas=1;
    scanf("%d", &nCase);
 
    while(nCase--){
        
        scanf("%d%d%d", &n,&m,&k);
 
		init();
		int minx = INF;
        int count=0;
		queue<int>Q;
 
		for(int i=1; i<=n; ++i){
		    if(arr[i]>=1 && arr[i]<=k){
		        Q.push(i);
                if(cnt[arr[i]]++ == 0){
                    ++count;
 
                }
		        while(count == k){
		            int tmp = i - Q.front() + 1;
		            minx = min(tmp, minx);
		            int val = arr[Q.front()];
		            if(--cnt[val]==0){
                        --count;
		            }
		            Q.pop();
 
		        }
		    }
		}
        printf("Case %d: ", cas++);
		if(minx == INF) puts("sequence nai");
		else printf("%d\n", minx);
    }
    return 0; 
}