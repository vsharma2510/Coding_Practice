//Testing code to delete text file within C++ code
#include <fstream>
#include <iostream>
//#include <boost/filesystem.hpp>
#include "TString.h"
#include <stdio.h>

using namespace std;
//using namespace boost;
int main(){
  
  //filesystem::path file_name;
  TString file_name = Form("test_file.txt");
  //ofstream test_file;
  std::remove(file_name.Data());
  ofstream test_file;
  test_file.open(file_name,std::ofstream::app);
  test_file<<"test"<<"\n";
  test_file.close();
 
  cout<<"Done"<<endl;
  return 0;
}
  
