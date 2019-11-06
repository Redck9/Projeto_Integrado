from pyprimes import *

def sequence_exists(l,ls,limit = 100):
    for x in range(0,len(ls)-l):
        if x+l > len(ls): return False
        if any (ls[i] > limit/6 for i in range(x,x+l,1)) :
            return False
        test_sum = sum(ls[x:x+l:1])
        if (test_sum <limit) and is_prime(test_sum) :
            return True
    return False

def main():
    n = prime_count(10000)
    prime_list = list(nprimes(n))
    l = 6
    for x in range(6,len(prime_list)):
        if sequence_exists(x,prime_list,10000):
            l=x
    print l

if __name__ == '__main__':
    main()
