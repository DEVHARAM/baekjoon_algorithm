
#include <iostream>
#include <algorithm>
using namespace std;

bool visit[26][26]={false,};
int apart[26][26];
int house=1;
void bfs(int x,int y,int count){
    int dx[]={0,-1,0,1};
    int dy[]={-1,0,1,0};
    int nx;
    int ny;
    for(int i=0;i<4;i++){
        nx=x+dx[i];
        ny=y+dy[i];
        if(nx<0 || ny<0 || nx>=count || ny>=count)
            continue;
        if(visit[nx][ny]==false && apart[nx][ny]==1){
            visit[nx][ny]=true;
            house+=1;
            bfs(nx,ny,count);
        }
    }
}

int main()
{
    int count;
    int result[50];
    int k=0;
    scanf("%d",&count);
    
    for(int i=0;i<count;i++){
        for(int j=0;j<count;j++){
            scanf("%1d",&apart[i][j]);
        }
        
    }    
    for(int i=0;i<count;i++){
        for(int j=0;j<count;j++){
            if(visit[i][j]==false && apart[i][j]==1){
                visit[i][j]=true;
                bfs(i,j,count);
                result[k++]=house;
                house=1;
            }
        }
    }
    printf("%d\n",k);
    sort(result,result+k);
    for(int i=0;i<k;i++){
        printf("%d\n",result[i]);
    }
    return 0;
}