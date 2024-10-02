#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import sys

def fibonacci(upper=100):
	# initialize fibonacci sequence
	sequence = [0,1]
	next_fib = 1
	# set up loop if last number is less than the upper limit defined
	while next_fib <= upper:
		sequence.append(next_fib)
		next_fib += sequence[len(sequence)-2]
	return sequence

if __name__ == "__main__":
    print(fibonacci())