def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def primRoots(modulo):
    roots = []
    required_set = set(num for num in range(1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots



def publickey(a, alpha, q):
    key = pow(alpha, a) % q
    return key


def secretkey(y, x, q):
    K = pow(y, x) % q
    return K


if __name__ == "__main__":
    q = 19
    # Select xa and xb < q
    xa = 13
    xb = 7
    primitive_roots = primRoots(q)
    alpha = primitive_roots[0] #Use the first primitive root for calculations
    pukeya = publickey(a=xa, alpha=alpha, q=q)
    pukeyb = publickey(a=xb, alpha=alpha, q=q)
    askey = secretkey(y=pukeyb, x=xa, q=q)
    bskey = secretkey(y=pukeya, x=xb, q=q)
    print(f"Public key of A is {pukeya} and public key of B is {pukeyb}")
    print(f"Secret key of A is {askey} and secret key of B is {bskey}")
    print(primitive_roots)

