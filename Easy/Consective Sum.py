def Con_Sum(N):
    count = 0
    L = 1
    num_list = []
    while( L*(L + 1.0) < 2.0*N):
        a = (2.0*N - L*(L+1.0)) / (2.0*(L+1))
        if (a - int(a) == 0.0):
            count += 1
            num_list.append(int(a))
        L += 1
    return count,num_list
