#include <iostream>
using namespace std;

class Rectangle {
  // int width,height;
public:
  Rectangle();
  Rectangle(int,int); // have to declare constructors here
  int width,height;
  int area(void){return width*height;}
};

Rectangle::Rectangle(int a,int b) : width(a), height(b) {}

Rectangle::Rectangle(){
  width=5;
  height=5;
}

int area(int x, int y){
  return 2*(x+y);
}

int main(){
  Rectangle rect(3,4); //have to pass arguments here
  Rectangle rect1;
  //rect.set_values(3,4);
  cout<<"area: "<<rect.area()<<endl;
  cout<<"area: "<<area(rect.width,rect.height)<<endl;
  cout<<"area: "<<rect1.area()<<endl;
  return 0;
}
