//g++  5.4.0

#include <iostream>
#include <algorithm>
using namespace std;

void back(int num[],int arr[],bool use[],int k,int start,int count){
    if(k==6){
        for(int i=0;i<6;i++){
            printf("%d ",num[arr[i]-1]);
        }
        printf("\n");
        return;
    }
    for(int i=start;i<count+1;i++){
        if(use[i]==false){
            arr[k]=i;
            use[i]=true;
            back(num,arr,use,k+1,i+1,count);
            use[i]=false;
        }
    }
}

int main()
{
    int count;
    while(true){
        cin>>count;
        if(count==0){
            break;
        }
        int num[count];
        for(int i=0;i<count;i++){
            cin>>num[i];
        }
        int arr[6]={0,};
        bool use[count+1]={false,};
        back(num,arr,use,0,1,count);
        printf("\n");
        
    }
    
    return 0;
}