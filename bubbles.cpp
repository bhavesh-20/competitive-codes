#include<bits/stdc++.h>

using namespace std;

int _mergeSort(int arr[], int temp[], int left, int right); 
int merge(int arr[], int temp[], int left, int mid, int right); 
  

int mergeSort(int arr[], int array_size) 
{ 
    int temp[array_size]; 
    return _mergeSort(arr, temp, 0, array_size - 1); 
} 

int _mergeSort(int arr[], int temp[], int left, int right) 
{ 
    int mid, inv_count = 0; 
    if (right > left) { 
        mid = (right + left) / 2; 
        inv_count += _mergeSort(arr, temp, left, mid); 
        inv_count += _mergeSort(arr, temp, mid + 1, right); 
        inv_count += merge(arr, temp, left, mid + 1, right); 
    } 
    return inv_count; 
} 
  
int merge(int arr[], int temp[], int left, 
          int mid, int right) 
{ 
    int i, j, k; 
    int inv_count = 0; 
    i = left; 
    j = mid; 
    k = left;
    while ((i <= mid - 1) && (j <= right)) { 
        if (arr[i] <= arr[j]) { 
            temp[k++] = arr[i++]; 
        } 
        else { 
            temp[k++] = arr[j++]; 
            inv_count = inv_count + (mid - i); 
        } 
    } 
    while (i <= mid - 1) 
        temp[k++] = arr[i++]; 
    while (j <= right) 
        temp[k++] = arr[j++];
    for (i = left; i <= right; i++) 
        arr[i] = temp[i]; 
  
    return inv_count; 
}  

int main(){
    int t;
    scanf("%d",&t);
    while(t!=0){
        int n,i,j,cnt=0,c=0;
        n=t;
        int a[n];
        for(i=0;i<n;i++)
        scanf("%d",&a[i]);
        cnt=mergeSort(a,n);
        if(cnt%2==0)
        printf("Carlos\n");
        else
        printf("Marcelo\n");
        scanf("%d",&t);
    }
}