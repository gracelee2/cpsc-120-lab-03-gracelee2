// Grace Lee
// CPSC 120-01
// 2021-09-23
// grace1@csu.fullerton.edu
// @gracelee2
//
// Lab 03-02
//
// This lab uses 3 loops to print out a pattern
//
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  // TODO: Declare a const int named kCounterMax and initialize it to 22.
const int kCounterMax = 22;
  // TODO: Write an outer loop which starts from 0 and goes up to the counter
  // max.
for(int for_counter = kCounterMax; for_counter >=1; for_counter--){
  for(int second_counter = kCounterMax- for_counter; second_counter > 0; second_counter--){
    cout << "*";
  }
for(int third_counter = for_counter; third_counter>0;third_counter--){
  cout << "|";
}
cout << endl;

  }
  //for(int third_counter = 0; third_counter < for_counter; third_counter++){

  //}

  // TODO: Write an inner loop which starts from the current line number and
  // counts down to zero. Make sure that this loop is inside the outer loop.

  // TODO: Print an asterisk.

  // TODO: Write another inner loop which starts from the current line number
  // and counts up to the counter max. Make sure that this loop is inside the
  // outer loop but outside the first inner loop.

  // TODO: print a new line character

  return 0;
}
