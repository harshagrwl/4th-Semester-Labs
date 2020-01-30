#include<iostream>

using namespace std;

int calci(int a,int b,char c)
{
	char x;
	switch(c)
	{
		case '+':cout<<a+b<<endl;
		break;
		case '-':cout<<a-b<<endl;
		break;
		case '*':cout<<a*b<<endl;
		break;
		case '/':cout<<a/b<<endl;
		break;
		default :cout<<"wrong operator entered"<<endl;

	}

	cout<<"If you want to continue the operation the press 'Y' or else press 'N'"<<endl;
	cin>>x;

	return x;
}

int main()
{
	char x='Y',c;
	double a,b;

	for(;x=='Y';)
	{
		cout<<"Enter the first number:"<<endl;
		cin >>a;
		cout<<"Enter the operator"<<endl;
		cin >>c;
		cout<<"Enter the second number:"<<endl;
		cin >>b;

		x=calci(a,b,c);

	}

}