# CPSC 120

## Count to Ten

Computers are machines. And machines are great at doing repetitive tasks with precision and speed. Consider all the software that you use regularly and you'll realize that the programs you use are repeating algorithms, calculations, sorts, etc.

The construct that we use in programming to make a program repeat parts of itself is called a loop. A loop takes advantage of conditions similar to our `if-else-if-else` constructs and branching. Normally, a program runs by going one line at a time starting from the first line at the top of the file and ending at the last line at the bottom of the file. If we could find a way to be in the middle of our program and then jump backwards so we could repeat a part of a program, we'd have what's called a loop.

In programming each time the body of a loop repeats, it is called an iteration. It is very common to hear programmers use the verb _to iterate_ to mean the samething as _to repeat_.

In C++, there are many kinds of loops. We shall focus on three classic loops which appear in most languages you'll encounter in your academic career.

The three loops that we will use in this exercise are the [for loop](https://en.cppreference.com/w/cpp/language/for), the [while loop](https://en.cppreference.com/w/cpp/language/while), and the [do-while loop](https://en.cppreference.com/w/cpp/language/do). Each loop does the same thing as the other, yet a programmer may find one loop fits more elegantly than another.

In this exercise, we shall focus on counting. This means that our loops shall be used to change an integer variable over and over again to demonstrate to us a very simple way we can use loops to count for us. We shall write three loops which count ten numbers, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, and print them out to the terminal.

The [while loop](https://en.cppreference.com/w/cpp/language/while) has a very simple structure. You must always declare your state variable (the variable we'll use to count) outside of the loop and initialize it to the first number you wish to count. The loop has a single keyword `while` and uses a condition just like an `if` statement. Here's an example that counts five numbers, starting from 0 and ending at 4, printing each number to the terminal.

```c++
int state = 0;
while (state < 5) {
  cout << "State is currently: " << state << "\n";
  state = state + 1;
}
```

Note that in a while loop, if the condition `state < 5` isn't true, then the loop will not execute. This little gotcha catches quite a few beginning programmers.

The [do-while loop](https://en.cppreference.com/w/cpp/language/do) has a very similar structure to a while loop. The most important detail about a do-while loop is that it is guaranteed to always run at least once. The loop has two keywords, `do` and `while`. You must always declare your state variable (the variable we'll use to count) outside of the loop and initialize it to the first number you wish to count. The condition is just like an `if` statement except it is checked at the end of the loop. Here's an example that counts five numbers, starting from 0 and ending at 4, printing each number to the terminal.

```c++
int state = 0;
do {
  cout << "State is currently: " << state << "\n";
  state = state + 1;
} while (state < 5);
```

The last loop for this exercise is called a [for loop](https://en.cppreference.com/w/cpp/language/for). The for loop is very similar to the while loop. Instead of declaring and initializing the state variable outside of the loop and updating the state variable in the loop body, a for loop lets you do those two operations and check the loops condition all on one line. There is only one keyword, `for`, just like a while loop. Here's an example that counts five numbers, starting from 0 and ending at 4, printing each number to the terminal.

```c++
for (int state = 0; state < 5; state++) {
  cout << "State is currently: " << state << "\n";
}
```

Notice that the state variable `state` is initialized and declared on the same line as the for loop. Inside the parentheses of the for loop, three things are defined. The first is the declaration and initialization of the state variable, the next is the loops condition, and finally the state variable is updated every time the loop repeats (every iteration).

The [double plus sign `++`](https://en.cppreference.com/w/cpp/language/operator_incdec) is an operator that allows us to add one to a variable. Similarly the double minus sign `--` is an operator that allows us to subtract one from a variable. Be very careful with these operators because they are easy to misuse.


You may see people online using [`goto` statements](https://en.cppreference.com/w/cpp/language/goto) in lieu of loops. You should consider these souls as bordering on criminal insanity since the [goto statement is considered harmful](https://dl.acm.org/doi/10.1145/362929.362947). Don't ever use `goto` because it is one of many things that are [considered harmful in computer science](https://en.wikipedia.org/wiki/Considered_harmful). (Regrettably, [C++ is considered harmful](http://harmful.cat-v.org/software/c++/) by many.)


## Requirements

Write a program that counts from 0 to 9 (10 numbers) using a while loop, do-while loop, and a for loop. There is nothing for the computer user to enter. Every time the program runs it prints out 0 through 9 three times.

Use a constant integer to define the maximum number of iterations each loop will execute. Use this constant in the condition for each loop.

You shall use [cout](https://en.cppreference.com/w/cpp/io/cout) to print messages to the terminal.
Each iteration print to the terminal the value of the state variable.

Each loop shall use a different state variable.

The starting code defines a series of `TODO` comments which you can use to formulate your plan and develop your program.

Write your program progressively. Compile your program often and check that you're making progress. Make sure your program behaves the way you expect.

The output of your program must match the output given in the section Example Output below.

To compile your program, you use the `make` command. A Makefile is provided for this exercise.

The Makefile has the following targets:
  
* all: builds the project
* clean: removes object and dependency files
* spotless: removes everything the clean target removes and all binaries
* format: outputs a [`diff`](https://en.wikipedia.org/wiki/Diff) showing where your formatting differes from the [Google C++ style guide](https://google.github.io/styleguide/cppguide.html)
* tidy: output of the [linter](https://en.wikipedia.org/wiki/Lint_(software)) to give you tips on how to improve your code
* headercheck: check to make sure your files have the appropriate header

## Don't Forget

Please remember that:

- You need to put a header in every file.
- You need to follow the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html).
- Remove the `TODO` comments.

## Testing Your Code

Computers only ever do exactly what they are told, exactly the way they are told it, and never anything else. Testing is an important process to writing a program. You need to test for the program to behave correctly and test that the program behaves incorrectly in a predictable way.

As programmers we have to remember that there are a lot of ways that we can write the wrong program and only one to a few ways to write the correct program. We have to be aware of [cognitive biases](https://en.wikipedia.org/wiki/List_of_cognitive_biases) that we may exercise that lead us to believe we have correctly completed our program. That belief may be incorrect and our software may have errors. [Errors in software](https://www.wired.com/2005/11/historys-worst-software-bugs/) may lead to loss of [life](https://www.nytimes.com/2019/03/14/business/boeing-737-software-update.html), [property](https://en.wikipedia.org/wiki/Mariner_1), [reputation](https://en.wikipedia.org/wiki/Pentium_FDIV_bug), or [all of the above](https://en.wikipedia.org/wiki/2009%E2%80%9311_Toyota_vehicle_recalls).

### Test strategy

Start simple, and work your way up. Good tests are specific, cover a broad range of fundamentally different possibilities, can identify issues quickly, easily, and directly, without need for much set up, and can almost be diagnosed by inspection if the code fails to execute the test correctly.

## Example Output

Please ensure your program's output is identical to the example below.

```
$ make
set -e; clang++ -MM -g -Wall -pipe -std=c++14  count_to_ten.cc \
	| sed 's/\(count_to_ten\)\.o[ :]*/\1.o count_to_ten.d : /g' > count_to_ten.d; \
	[ -s count_to_ten.d ] || rm -f count_to_ten.d
clang++ -g -Wall -pipe -std=c++14  -c count_to_ten.cc
clang++ -g -Wall -pipe -std=c++14 -o count_to_ten count_to_ten.o 
$ ./count_to_ten 
With a for loop
0
1
2
3
4
5
6
7
8
9

With a while loop
0
1
2
3
4
5
6
7
8
9

With a do-while loop
0
1
2
3
4
5
6
7
8
9
```

