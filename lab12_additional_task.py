import time
import math

with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()

d = 256

P = 0.001
n = 20
b = int(math.ceil(-n * math.log(P) / (math.log(2)**2)))
k = int(math.ceil(b/n * math.log(2)))

def is_prime(p):
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def get_primes(k, start=101):
    primes = []
    while len(primes) < k:
        if is_prime(start):
            primes.append(start)
            
        start += 1
    
    return primes

def rk_hash(word, q):
    hw = 0
    for i in range(len(word)):
        hw = (hw*d + ord(word[i])) % q
    return hw

def bloom_insert(word, bloom, primes, b):
    for q in primes:
        h = rk_hash(word, q)
        bloom[h % b] = 1
        
def bloom_check(word, bloom, primes, b):
    for q in primes:
        h = rk_hash(word, q)
        if bloom[h % b] == 0:
            return False
    
    return True

def rabin_karp_bloom(S, patterns):
    M = len(S)
    N = len(patterns[0])
    counter = 0
    comparison = 0
    colision = 0
    t_start = time.perf_counter()
    
    primes = get_primes(k)
    bloom = [0 for _ in range(b)]
    for patern in patterns:
        bloom_insert(patern, bloom, primes, b)
    
    for m in range(M-N+1):
        comparison += 1
        if bloom_check(S[m:m+N], bloom, primes, b):
            if S[m:m+N] in patterns:
                counter += 1
            else:
                colision += 1
            
    t_stop = time.perf_counter()
    time_elapsed = t_stop - t_start
    return counter, comparison, colision, time_elapsed

patterns = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 
            'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 
            'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 
            'baggins', 'further']

print('Bloom dla jednego wzorca')
res_rkb = rabin_karp_bloom(S, ['gandalf'])
print(f"{res_rkb[0]}; {res_rkb[1]}; {res_rkb[2]}; {res_rkb[3]:.7f}")
print('Bloom dla wielu wzorców')
res_rkb = rabin_karp_bloom(S, patterns)
print(f"{res_rkb[0]}; {res_rkb[1]}; {res_rkb[2]}; {res_rkb[3]:.7f}")