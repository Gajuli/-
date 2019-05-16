import random as rnd

def expmod(base, exp, m):
	if exp == 0:
		return 1
	elif exp%2 == 0:
		return (expmod(base, exp//2, m))**2 % m
	else:
		return (base * expmod(base, exp-1, m)) % m
		
		
def fermat_test(n):
	a = rnd.randint(2, n-1)
	return expmod(a, n-1, n) == 1
	

def is_prime(n, max_test):
    for test in range(max_test):
        if not fermat_test(n):
            return False
    return True


def find_primes(max_num, max_test, required=-1):
	primes = []
	for num in range(max_num, 2, -1):
		if is_prime(num, max_test):
			primes.append(num)
		if required >= 0 and len(primes) >= required:
			break
	return primes
