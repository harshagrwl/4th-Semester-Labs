#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    pid_t childpid;
    int i, fib_sum=0, fib1=1, fib2=1, temp=1, status;

    int fd[2];
    int val = 0;

    // create pipe descriptors
    pipe(fd);

    childpid = fork();
    if(childpid != 0)  // parent
    {
        close(fd[1]);
        // read the data (blocking operation)
        read(fd[0], &val, sizeof(val));

        printf("Parent received value: %d\n", val);
        // close the read-descriptor
        close(fd[0]);
    }
    else  // child
    {
        // writing only, no need for read-descriptor:
        close(fd[0]);

        for(i=1; i<=5; i++)
        {
            temp=temp*i;
        }

        // send the value on the write-descriptor:
        write(fd[1], &temp, sizeof(temp)); 
        printf("Child send value: %d\n", temp);

        // close the write descriptor:
        close(fd[1]);

        return temp;
    }
}