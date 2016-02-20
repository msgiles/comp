import collections

def swapchars(s):
	t = ''.join(e for e in s if e.isalnum())
	c = collections.Counter(t)
	common = c.most_common()
	return s.replace(common[0][0], common[-1][0])

print swapchars('It was the best of times, it was the worst of times.')
print swapchars('I\'m just a chi-town coder with a nice flow.')

def sortcat(_n_, *argv):
	s = sorted(argv, key=len, reverse=True)
	if _n_ == -1:
		s = s
	else:
		s = s[0:_n_ ]	
	return ''.join(s)

print sortcat(1, 'abc', 'bc')
print sortcat(2, 'bc', 'c', 'abc')

def createstates():
	abbrev = {}
	with open('states.txt') as f:
		for line in f:
			(val, key) = line.split(',')
			abbrev[key.strip('\n')] = val
	return abbrev

def abbrevtoname(abbrev):
	states = createstates()
	return states[abbrev]

print abbrevtoname("PA")

def nametoabbrev(name):
	states = createstates()
	r = "No matches"
	for key, val in states.iteritems():
		if val == name:
			r = key
	return r

print nametoabbrev("Nebraska")

