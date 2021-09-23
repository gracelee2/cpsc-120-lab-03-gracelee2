// Grace Lee
// CPSC 120-01
// 2021-09-23
// grace1@csu.fullerton.edu
// @gracelee2
//
// Lab 03-01
//
// This lab uses different types of loop to count from 0 to 9
//
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  // TODO: Declare a const int kCounterMax and initailize it to 10
  const int kCounterMax = 10;
  cout << "With a for loop\n";

  for (int for_counter = 0; for_counter < kCounterMax; for_counter++) {
    cout << for_counter << "\n";
  }

  cout << "\nWith a while loop\n";

  int while_counter = 0;
  while (while_counter < kCounterMax) {
    cout << while_counter << "\n";
    while_counter = while_counter + 1;
  }
  cout << "\nWith a do-while loop\n";
  // TODO: Write a do-while loop which prints out the numbers 0 through 9 with
  // each number on a line by itself. Use kCounterMax to control the loop.
  // Declare as many variables as you need.
  int dowhile_counter = 0;
  do {
    cout << dowhile_counter << "\n";
    dowhile_counter++;
  } while (dowhile_counter < kCounterMax);

  return 0;
}
