#include <iostream>
using namespace std;

int main(){
  int *x;
  x = new int[2];
  x[1]=1;
  x[2]=2;
  cout<<x[1]<<" "<<x[2]<<endl;
  return 0;
}
