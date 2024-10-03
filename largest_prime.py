#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""
import argparse
parser = argparse.ArgumentParser(description = 'Generate a Fibonacci sequence up to a defined upper limit and output the largest prime number in that sequence')
parser.add_argument('-u','--upper', help = 'upper limit of sequence to check')
args = parser.parse_args()

import fibonacci

def prime(number):
	prime_flag = True
	# check if there are any factors other than number itself and 1; start at 2
	for i in range(2,number-1):
		# prime_flag is set false if a factor is found, otherwise remains true
		if number%i == 0:
			prime_flag = False
			break
	return prime_flag

if __name__ == "__main__":
	args.upper = int(args.upper)
	# generate sequence of numbers to check
	check_prime = fibonacci.fibonacci(args.upper)
	for i in range(1, len(check_prime)):
		# check starting from end of list i.e. largest number
		if prime(check_prime[-i]) == True:
			print(check_prime[-i])
			break
