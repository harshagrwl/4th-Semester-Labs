#include<stdio.h>
void main()
{
   int bt[10],ct[10],at[10]={0},turnaroundtime[10],i,j,n,wt[10];
   float atat=0,awt=0;
   printf("\nEnter number of processes:");
   scanf("%d",&n);
   printf("\nEnter burst time of processes:");
   for(i=0;i<n;i++){    
      printf("\nP%d:",i+1);
      scanf("%d",&bt[i]);
   }
   printf("\nEnter arrival time of processes:");
   for(i=0;i<n;i++){
      printf("\nP%d:",i+1);
      scanf("%d",&at[i]);
   }
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