#include <stdio.h>
#include <stdlib.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int n;
	    int k=20;
	    scanf("%d",&n);
	    if(n%2==0){
	        long long int m=1,next,prev=0,sum=0,prev_checker=0,next_checker=0,corc=0;
	        while(k--){
	            if(m==1){
	                m*=2;
	                printf("1 %lld\n",m-1);
	                fflush(stdout);
	                scanf("%lld",&next);
	                next_checker=n*(m-1)-next;
	                if(next%2!=0) sum+=1;
	                prev=next-sum;
	            }
	            else{
	                m*=2;
	                printf("1 %lld\n",m-1);
	                fflush(stdout);
	                scanf("%lld",&next);
	                next_checker=n*(m-1)-next;
	                long long int check=(prev-next+sum);
	                if(check<0) check=check*-1;
	                check=check/(m/2);
	                if((((n-check))/2)%2!=0){
	                    sum+=(m/2);
	                }
	                prev=next-sum;
	            }
	            //printf("next_checker=%ld prev_checker=%ld prev=%ld next=%ld\n",next_checker,prev_checker,prev,next);
	           /* if(prev_checker==next_checker){
	                printf("2 %lld\n",sum);
	                fflush(stdout);
	                int z;
	                scanf("%d",&z);
	                corc=1;
	                if(z==1) break;
	                else
	                exit(1);
	            }
	            else prev_checker=next_checker;
	            */
	        }
	        if(corc==0){
	            printf("2 %lld\n",sum);
	                fflush(stdout);
	                int z=0;
	                scanf("%d",&z);
	                if(z==-1)
	                exit(0);
	        }
	    }
	    else{
	        long long int next_checker,prev_checker=0,prev=0,next,sum=0,sum_1=0,corc=0,m=1;
	        while(k--){
	            m*=2;
	            printf("1 %lld\n",m-1);
	            fflush(stdout);
	            scanf("%lld",&next);
	            next_checker=n*(m-1)-next;
	            if(m==2){
	                if(next%2==0){
	                    sum+=1;
	                }
	                else sum_1+=1;
	                prev=next-sum_1;
	            }
	            else{
	                long long int check=prev-next+sum_1;
	 
	                
	                check=check/(m/2);
	                //printf("%lld\n",check);
	                if(check<0){
	                   check=check+n;
	                   check/=(2);
	                   if(check%2==1) sum+=(m/2);
	                   else sum_1+=(m/2);
	                }
	                else{
	                    check=n-check;
	                    check/=2;
	                    if(check%2==0) sum+=(m/2);
	                    else sum_1+=(m/2);
	                }
	                //printf("sum_1=%lld\n",sum_1);
	                prev=next-sum_1;
	                //printf("next_checker=%ld prev_checker=%ld prev=%ld next=%ld check=%lld\n",next_checker,prev_checker,prev,next,check);
	            }
	            
	            /*if(prev_checker==next_checker){
	                printf("2 %lld\n",sum);
	                fflush(stdout);
	                int z=0;
	                corc=1;
	                scanf("%d",&z);
	                if(z==1) break;
	                else 
	                exit(0);
	            }
	            else prev_checker=next_checker;*/
	        }
	        if(corc==0){
	            printf("2 %lld\n",sum);
	                fflush(stdout);
	                int z=0;
	                scanf("%d",&z);
	                if(z==-1)
	                exit(0);
	                
	               
	        }
	    }
	}
	return 0;
}

