#include<stdio.h>
#include<stdlib.h>
#include<sys/wait.h>
#include<unistd.h>
int main(){
 int pfds[2];
 int n,f=1,i,n1;
 pipe(pfds);
 if(!fork()){
  printf("Child Process currently active \n");
  printf("Enter the Number:");
  scanf("%d",&n);
  for(i=1;i<=n;i++)
   f=f*i;
  write(pfds[1],(char *)&f,sizeof(f));
  close(pfds[1]);
  printf("Child process exiting\n");
 }
 else
 {
  
  printf("Parent process currently active\n");
  read(pfds[0],&n1,sizeof(int));
  printf("The factorial value is :%d\n",n1);
  close(pfds[0]);
 }
 return 0;
}
