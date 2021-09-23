
#include <Magick++.h>

#include <cstdlib>
#include <iostream>

using namespace std;
using namespace Magick;

int main(int argc, char const* argv[]) {
  InitializeMagick(*argv);
  // Some colors that you can use.
  ColorRGB white{1, 1, 1};
  ColorRGB red{1, 0, 0};
  ColorRGB blue{0, 0, 1};
  ColorRGB orange{1, 0.647, 0};
  ColorRGB black{0, 0, 0};
  // The dimension must be multiples of 64. Please do not change this.
  const int kDim = 8 * 64;
  InitializeMagick(*argv);
  // Square image that is kDim by kDim; set the color to white for debugging.
  Image image(Geometry(kDim, kDim), white);

  // TODO: Write the algorithm using two nested for loops as described in the
  // README.

  // Examples of how to set the color of a pixel. Feel free to remove this
  // example code.
  int row = 100;
  int column = 100;
  image.pixelColor(row, column, blue);
  row = 400;
  column = 450;
  image.pixelColor(row, column, orange);
  // End exampple code

  image.write("checkerboard.png");
  return 0;
}
