#include<bits/stdc++.h>
using namespace std;
int nthpal(int num)
{
    int cnt = 0,latest,i=1;
    while(cnt < num)
    {
    int num1 = i;
    int rem;
    int rev = 0;
    while(num1 != 0)
    {
        rem = num1 % 10;
        num1 = num1 / 10;
        rev = rev*10 + rem;
    }
    //cout<<rev<<endl;
    if(i == rev)
    {
        latest = i;
        cnt += 1;
        cout<<latest<<endl;

    }
    i += 1;
    }
    return latest;
    
}
int main ()
{
    int num = 78;
    int pal = nthpal(num);
    cout<<num<<"th pallindrome number: "<<pal<<endl;
    return 0;
}