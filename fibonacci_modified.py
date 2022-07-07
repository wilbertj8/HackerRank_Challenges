def fibonacciModified(t1, t2, n):
    res = 0
    for i in range(2, n):
        res = t1 + t2*t2
        t1, t2 = t2, res
    return res