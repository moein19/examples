from app import prime

def odd_even_prime(first,second):
    d = {"even":[],"odd":[],"prime":[]}
    for i in range(first,second+1):
        if i % 2 == 0:
            d["even"].append(i)
        elif i % 2 != 0:
            d["odd"].append(i)
        if prime(i):
            d["prime"].append(i)
    return d