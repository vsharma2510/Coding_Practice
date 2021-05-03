#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;
int main(){
  
  double x,y,r;
  double square=0,circle=0;
  srand(time(0));
  cout<<"RAND_MAX is "<<RAND_MAX<<endl;
  int n=1000000;

  for(int i=0;i<n;i++){
    x=(double)rand()/RAND_MAX;
    y=(double)rand()/RAND_MAX;
    //cout<<"x is "<<x<<" y is "<<y<<endl;
    r=(x*x)+(y*y);
    if(r<1){circle++;}
    if(r>1){square++;}
  }

  cout<<"value of r is "<<r<<endl;
  cout<<"value of pi is "<<(4*(circle/n))<<endl;

  return 0;
}
