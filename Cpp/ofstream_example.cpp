// ofstream::open / ofstream::close
#include <fstream>      // std::ofstream
using namespace std;
int main () {

  std::ofstream ofs;
  ofs.open ("./output/ofstream_test.txt", std::ofstream::app);

  ofs << " more lorem ipsum \n";

  ofs.close();

  return 0;
}
