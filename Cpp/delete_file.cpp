//Testing code to delete text file within C++ code
#include <fstream>
#include <boost/filesystem.hpp>
#include "TString.h"



using namespace std;

int main(){
  
  TString file_name = Form("test_text_file.txt");
  ofstream test_file;
  test_file.open(file_name,std::ofstream::app);
  test_file<<"test"<<"\n";
  test_file.close();

  return 0;
}
  
