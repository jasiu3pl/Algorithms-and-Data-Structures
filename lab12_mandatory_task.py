import time

with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()
W = 'time.'

M = len(S)
N = len(W)

def naive(S, W):
    M = len(S)
    N = len(W)
    counter = 0
    comparison = 0
    t_start = time.perf_counter()
    
    m = 0
    while m <= M - N:
        i = 0
        while i < N:
            comparison += 1
            if S[i+m] == W[i]:
                i += 1
                continue
            break
        m += 1     
        if i == N:
            counter += 1
            
    t_stop = time.perf_counter()
    time_elapsed = t_stop - t_start
    
    return counter, comparison, time_elapsed

d = 256 
q = 101

def rk_hash(word):
    hw = 0
    for i in range(N):
        hw = (hw*d + ord(word[i])) % q
    return hw

def rabin_karp(S, W):
    M = len(S)
    N = len(W)
    counter = 0
    comparison = 0
    colision = 0
    t_start = time.perf_counter()
    
    hW = rk_hash(W)
    m = 0
    while m <= M - N:
        hS = rk_hash(S[m:m+N])
        comparison += 1
        if hS == hW:
            if S[m:m+N] == W:
                counter += 1
            else:
                colision += 1
        m += 1        
   
    t_stop = time.perf_counter()
    time_elapsed = t_stop - t_start
    return counter, comparison, colision, time_elapsed

def rabin_karp_rolling(S, W):
    M = len(S)
    N = len(W)
    counter = 0
    comparison = 0
    colision = 0
    t_start = time.perf_counter()
    
    h = 256**(N-1) % q
    hW = rk_hash(W)
    hS = rk_hash(S[0:N])
    for m in range(M-N+1):
        comparison += 1
        if hS == hW:
            if S[m:m+N] == W:
                counter += 1
            else:
                colision += 1
        if m < M-N:
            hS = ((d * (hS - (ord(S[m]) * h))) + ord(S[m+N])) % q
            
    
    t_stop = time.perf_counter()
    time_elapsed = t_stop - t_start
    return counter, comparison, colision, time_elapsed
    

res_naive = naive(S, W)
res_rk = rabin_karp(S, W)
res_rkr = rabin_karp_rolling(S, W)
print('Naive')
print(f"{res_naive[0]}; {res_naive[1]}; {res_naive[2]:.7f}")
print('Rabin-Karp')
print(f"{res_rk[0]}; {res_rk[1]}; {res_rk[2]}; {res_rk[3]:.7f}")
print('Rabin-Karp Rolling')
print(f"{res_rkr[0]}; {res_rkr[1]}; {res_rkr[2]}; {res_rkr[3]:.7f}")
