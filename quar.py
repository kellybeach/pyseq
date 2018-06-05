# Attempt to make the Quarter Number Sequence from Fib
#example on Python site, used Sage code on
#https://oeis.org/search?q=0%2C1%2C2%2C4%2C6%2C9%2C12&sort=&language=english&go=Search
#went back to Fib code and finished in about ten minutes
import dis
def quar(n):
	a, b  =  0, 1 #we explicitly define the first two inputs
	while a < n:
		print(a, end=' ') #prints all a vaues until loop terminates at input n
		a, b = a + b, a//b + 1 #the function is defined to replace a, b after first adding the terms, then taking
		#the integer floor of the quotient a/b and adding 1, then storing these two new values into a, b and repeating
	print()
quar(1000)
dis.dis(quar) # i added dis in an attempt to understand what was going on at the machine level to understand the loop
# after reading about psuedocode in Cox, O'Shea, Neil I figured out how simple it really was. The magic is in the a, b structure
#originaly, this was the add the right, down, left, up squares
#below is a visualization of the loop

#0, 1 := 1, 1
#1, 1 := 2, 2
#2, 2 := 4, 1
#4, 2 := 6, 3
#6, 3 := 9, 3
#9, 3 := 12, 4
#12, 4 := 16, 4
#...
