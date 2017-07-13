#!/usr/bin/env python3

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 3
	print('step 3')
	yield 5

o = odd()

def odd2():
	r = 'odd2()'
	n = yield r
	print('n = %s' % n)

o2 = odd2()
r = o2.send('o2')
print(r)