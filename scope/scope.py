a = 0	# global スコープ

def f():
	print(a)

def g():
	a = 1	# local スコープ

f()
g()
print(a)