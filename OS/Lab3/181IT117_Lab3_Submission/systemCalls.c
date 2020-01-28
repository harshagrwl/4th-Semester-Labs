#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
	printf("Child Process is not created. Before child process\n");

	int pid = fork();
	if (pid < 0)
	{
		printf("error occured while creating the child process\n");
		exit(0);
	}

	if (pid)
	{
		printf("Output From the parent process, with PID: %d\n", getpid());
		printf("Value which the fork() fuction returned: %d\n", pid);
		wait(NULL);
	}
	else
	{
		printf("Output From the child process, with PID: %d\n", getpid());
		char* arr[] = {"ls", "-l", NULL};
		if (execvp(arr[0], arr) == -1)
		{
			printf("Error during exec");
		}
		exit(0);
	}

	printf("After terminating the child process\n");
}