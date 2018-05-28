# Attempt to make the Quarter Number Sequence (A002620) from Fib
#example on Python site, used Sage code on
#https://oeis.org/search?q=0%2C1%2C2%2C4%2C6%2C9%2C12&sort=&language=english&go=Search
#went back to Fib code and finished in about ten minutes
def quar(n):
	a, b  =  0, 1
	while a < n:
		print(a, end=' ')
		a, b = a + b, a//b + 1 
	print()
quar(1000)

#originaly, this was the add the right, down, left, up squares
