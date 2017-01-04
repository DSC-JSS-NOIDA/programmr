#include<iostream>
using namespace std;
int main()
{
    int i, n;
    cin>>n;
    int A[n], s=0;
    for(i=0; i<n; i++)
    {
        cin>>A[i];
        s = s + A[i];
    }
    cout<<s;
    return 0;
}