#悪い実装例
#def numerical_diff(f, x):
#    h = 1e-50
#    return (f(x+h)-f(x)) / h

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)
