#include<stdio.h>

void fcfs(int n, int bt[], int at[]){
      int ct[10],turnaroundtime[10],i,j,wt[10];
   float atat=0,awt=0;
      ct[0]=bt[0]+at[0];
   for(i=1;i<n;i++){
      ct[i]=ct[i-1]+bt[i];
   }
   for(i=0;i<n;i++){
      turnaroundtime[i]=ct[i]-at[i];
      wt[i]=turnaroundtime[i]-bt[i];
      awt=awt+wt[i];
      atat=atat+turnaroundtime[i];
   }
   printf("Process Arrival Burst_Time Turn_Around_Time Waiting_Time\n");
   for(i=0;i<n;i++){
      printf("P%d      %d        %d             %d           %d\n",i+1,at[i],bt[i],turnaroundtime[i],wt[i]);
   }
   awt=awt/n;
   atat=atat/n;
   printf("Average waiting time:%.2f\nAverage Turn around time:%.2f",awt,atat);
}

void sjp(int limit, int burst_time[],int arrival_time[]){
   int temp[10];
      int i, smallest, count = 0, time;
      double wait_time = 0, turnaround_time = 0, end;
      float average_waiting_time, average_turnaround_time;
      for(i = 0; i < limit; i++){
         temp[i] = burst_time[i];
      }
   burst_time[9] = 9999;  
      for(time = 0; count != limit; time++)
      {
            smallest = 9;
            for(i = 0; i < limit; i++)
            {
                  if(arrival_time[i] <= time && burst_time[i] < burst_time[smallest] && burst_time[i] > 0)
                  {
                        smallest = i;
                  }
            }
            burst_time[smallest]--;
            if(burst_time[smallest] == 0)
            {
                  count++;
                  end = time + 1;
                  wait_time = wait_time + end - arrival_time[smallest] - temp[smallest];
                  turnaround_time = turnaround_time + end - arrival_time[smallest];
            }
      }
      average_waiting_time = wait_time / limit; 
      average_turnaround_time = turnaround_time / limit;
      printf("nnAverage Waiting Time:t%lfn", average_waiting_time);
      printf("Average Turnaround Time:t%lfn", average_turnaround_time);
}
 
int main()
{
      int i, limit, total = 0, x, counter = 0, time_quantum;
      int wait_time = 0, turnaround_time = 0, arrival_time[10], burst_time[10], temp[10];
      float average_wait_time, average_turnaround_time;
      printf("\nEnter Total Number of Processes: ");
      scanf("%d", &limit);
      x = limit;
      for(i = 0; i < limit; i++)
      {
            printf("\nEnter Details of Process[%d]", i + 1);
 
            printf("Arrival Time: ");
 
            scanf("%d", &arrival_time[i]);
 
            printf("Burst Time: ");
 
            scanf("%d", &burst_time[i]);
 
            temp[i] = burst_time[i];
      }
      printf("\nEnter Time Quantum:");
      scanf("%d", &time_quantum);
      printf("\n\nFor First Come first serve\n\n");
      fcfs(limit,burst_time,arrival_time);
      printf("\n\nFor SJP\n\n");
      sjp(limit,burst_time,arrival_time);
      printf("\n\nFor Round Robin\n\n");
      printf("\nProcess ID \t Burst Time\t Turn Around Time\t Waiting Time\n");
      for(total = 0, i = 0; x != 0;)
      {
            if(temp[i] <= time_quantum && temp[i] > 0)
	{
                  total = total + temp[i];
                  temp[i] = 0;
                  counter = 1;
            }
            else if(temp[i] > 0)
            {
                  temp[i] = temp[i] - time_quantum;
                  total = total + time_quantum;
            }
            if(temp[i] == 0 && counter == 1)
            {
                  x--;
                  printf("\nProcess[%d]\t\t%dt\t\t %d\t\t\t %d", i + 1, burst_time[i], total - arrival_time[i], total - arrival_time[i] - burst_time[i]);
                  wait_time = wait_time + total - arrival_time[i] - burst_time[i];
                  turnaround_time = turnaround_time + total - arrival_time[i];
                  counter = 0;
            }
            if(i == limit - 1)
            {
                  i = 0;
            }
            else if(arrival_time[i + 1] <= total)
            {
                  i++;
            }
            else
            {	
		i = 0;
            }
      }
 
      average_wait_time = wait_time * 1.0 / limit;
      average_turnaround_time = turnaround_time * 1.0 / limit;
      printf("\nAverage Waiting Time:t%f", average_wait_time);
      printf("\nAvg Turnaround Time:t%fn", average_turnaround_time);
      return 0;
}
