#include <stdio.h>
#define MAX 100
 

int move[4][2]={{0,1},{-1,0},{1,0},{0,-1}};

int area[MAX][MAX];
int a[MAX];//영역당 크기
int count=0;//영역 개수
int size;//영역 크기
int m;
int n;
int num;//사각형 개수
int counting(int x,int y);
int condition(int x,int y);
int main(){
    
    int left_x,left_y,right_x,right_y;
    scanf("%d %d %d\n",&m,&n,&num);
    for(int k=0;k<num;k++){
            scanf("%d %d %d %d\n",&left_x,&left_y,&right_x,&right_y);
           for(int i=left_x;i<right_x;i++){
               for(int j=left_y;j<right_y;j++){
                   area[i][j]=1;
               }
           } 
        
    }
    for(int i=0;i<m;++i){
        for(int j=0;j<n;++j){
            if(area[j][i]==0){
                size=0;
                counting(j,i);
                a[count]=size;
                count++;
            }
        }
    }
    for(int i=0;i<count;++i){
        for(int j=i;j<count;++j){
            if(a[i]>a[j]){
                int tmp;
                tmp=a[i];
                a[i]=a[j];
                a[j]=tmp;
            }
        }
    }
    printf("%d\n",count);
    for(int i=0;i<count;++i){
        printf("%d ",a[i]);
    }
    return 0;
    
}

int counting(int x,int y){
    area[x][y]=1;
    size++;
    for(int i=0;i<4;++i){
        if(condition(x+move[i][0],y+move[i][1])>0){
            counting(x+move[i][0],y+move[i][1]);
        }
    }
    return;
}
int condition(int x,int y){
    if(x<0||y<0||x>=n||y>=m)
        return -1;
    else if(area[x][y]>0)
        return -1;
    else
        return 1;
}