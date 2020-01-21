#include <bits/stdc++.h>
using namespace std;

#define firs first
#define sece second

float fcfs(pair<int, int> proc[], int n, int tb)
{
	int time = 0, tw = 0, tt = 0;
	for (int a = 0; a < n; a++)
	{
		tw += (time - proc[a].firs);
		time += proc[a].sece;
		cout << "The completion time is: " << time << endl;
		tt += (time - proc[a].firs);
	}
	
	float aw = (float) tw / n;
	float at = (float) tt / n;
	
	cout << "\nThe average waiting time is: " << aw << endl;
	cout << "\nThe average turnaround time is: " << at << endl;

	return aw;
}

float sjrf(pair<int, int> proc[], int n, int tb)
{
	for (int a = 0; a < n; a++)
	{
		proc[a].sece *= -1;
	}

	int time = 0, tt = 0;
	int ind = 0, done = 0;
	priority_queue< pair<int, int> > pq;
	while (done < n)
	{
		while (ind < n && proc[ind].firs <= time)
		{
			pq.push(make_pair(proc[ind].sece, ind));
			ind++;
		}
		
		pair<int, int> temp = pq.top();
		pq.pop();

		if (temp.first == -1)
		{
			time++;
			done++;
			tt += (time - proc[temp.second].firs);
			cout << "The completion time is: " << time << endl;
		}
		else
		{
			time++;
			temp.first++;
			pq.push(temp);
		}
	}
	
	float aw = (float) (tt - tb) / n;
	float at = (float) tt / n;
	
	cout << "\nThe average waiting time is: " << aw << endl;
	cout << "\nThe average turnaround time is: " << at << endl;

	return aw;
}

float rr(pair<int, int> proc[], int n, int q, int tb)
{
	for (int a = 0; a < n; a++)
	{
		proc[a].sece *= -1;
	}

	int time = 0, tt = 0;
	queue< pair<int, int> > pq;
	int ind = 0, done = 0;
	pair<int, int> curr;
	while (done < n)
	{
		while (ind < n && proc[ind].firs <= time)
		{
			pq.push(proc[ind++]);
		}
		
		curr = pq.front();
		pq.pop();
		
		if (curr.sece <= q)
		{
			time += curr.sece;
			cout << "The completion time is: " << time << endl;
			tt += (time - curr.firs);
			done++;
		}
		else
		{
			curr.sece -= q;
			time += q;
			
			while (ind < n && proc[ind].firs <= time)
			{
				pq.push(proc[ind++]);
			}
			pq.push(curr);
		}
	}
	
	float aw = (float) (tt - tb) / n;
	float at = (float) tt / n;
	
	cout << "\nThe average waiting time is: " << aw << endl;
	cout << "\nThe average turnaround time is: " << at << endl;

	return aw;
}

int main()
{
	int n;
	cout << "Please enter the number of processes: ";
	cin >> n;
	
	int q;
	cout << "Please enter the quantum time: ";
	cin >> q;
	
	cout << "Please enter the burst time and arrival Time of each Process respectively: ";
	int tb = 0;
	pair<int, int> proc[n];
	for (int a = 0; a < n; a++)
	{
		cin >> proc[a].sece >> proc[a].firs;
		tb += proc[a].sece;
	}
	sort(proc, proc + n);

	cout << endl;
	
	cout << "Computation of FCFS:" << endl;
	float f = fcfs(proc, n, tb);
	cout << endl;

	cout << "Computation of SJP:" << endl;
	float s = sjrf(proc, n, tb);
	cout << endl;

	cout << "Computation of Round Robin:" << endl;
	float r = rr(proc, n, q, tb);
	cout << endl;

	if (f <= s && f <= r)
	{
		cout << "FCFS is the most efficient" << endl;
	}
	else if (s <= f && s <= r)
	{
		cout << "SJP is the most efficient" << endl;
	}
	else if (r <= f && r <= s)
	{
		cout << "RR is the most efficient" << endl;
	}
}
