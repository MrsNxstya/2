def product(N):
    dob = 1
    if N == 0:
        return 1 
    if N % 2 == 0:
        for i in range(2, N + 1, 2):
            dob *= i
    else:
        for i in range(1, N + 1, 2):
            dob *= i
    return dob
