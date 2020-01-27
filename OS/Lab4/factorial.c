#include <stdio.h>
#include <stdlib.h>
int main(int argc,char *argv[]){
    pid_t pid;
    if(atoi(argv[1]) < 0){
        printf("You have entered a negative no.");
        exit(0);
    }
    pid = fork();
    if( pid < 0){
        printf("Child process can't be created");
        exit(0);
    }
    else if(pid == 0){
        printf("Inside Child Process\n");
        int f = 0;
        int n = atoi(argv[1]);
        int arr[n],sum[n];
        arr[0] = 1;
        int k = 2;
        for(int i = 1;i<n;i++){
            arr[i] = arr[i-1]*k;
            k++;
        }
        for(int j = 0;j<n;j++){
            sum[j] = 0; 
            for (int i=0; i<=j; i++) 
            { 
                printf(" %d ",arr[i]); 
                sum[j]+=arr[i]; 
            } 
            printf("\n"); 
        }
        exit(0);
    }
    else
    { 
        wait(NULL); 
        printf("Inside Parent Process\n");
        printf("Done\n"); 
    } 
}
