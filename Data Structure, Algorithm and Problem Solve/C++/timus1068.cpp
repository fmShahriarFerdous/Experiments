#include<iostream>
using namespace std;
int main()
{
int n;
cin>>n;
if(n>0)
{
    int sum = 0;
    for (int i=1;i<=n;i++)
        sum = sum + i;
    cout<<sum;
}
else
{
    int sum = 0;
    for(int i=n;i<=1;i++)
        sum = sum + i;
    cout<<sum;
}
}
