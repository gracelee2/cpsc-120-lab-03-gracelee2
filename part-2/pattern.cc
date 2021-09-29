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
  const int kCounterMax = 22;

  for (int for_counter = 0; for_counter < kCounterMax; for_counter++) {
    for (int second_counter = 0; second_counter < for_counter;
         second_counter++) {
      cout << "-";
    }
    cout << "*";
    for (int third_counter = for_counter; third_counter < kCounterMax;
         third_counter++) {
      cout << "|";
    }
    cout << endl;
  }

  return 0;
}
