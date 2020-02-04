#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int n;
int ans = 1;

int factorial(int n) 
{
    if (n == 0)
    { 
        return 0;
    }
    int pid = fork(); 
    if (pid == -1) {
        exit(0);
    }
    if (pid==0) { 
        printf("Process ID: %d\nParent Process ID: %d\nComputation done by this Process : %d\n",getpid(),getppid(),ans);
        ans *= n;
        n = n-1;
        factorial(n);
        exit(0);
    }
    else {
       wait(NULL);
    } 
    return 0;   
}


int main()
{
    printf("Enter the number: \n");
    scanf("%d",&n);
    if(n==0)
    {
        printf("No Child Processes Spawned.\nFactorial Computed: 1.\n");
    }
    if(n<0)
    {
        printf("Invalid Number Entered.\n");
        exit(0);
    }
    factorial(n); 
    return 0;
}