"""Exact entry construction and compressed Gram verification at 25072, 46192 and 47968.

Usage: mixed_entry.py --check, or mixed_entry.py ORDER ROW COLUMN (zero-based).
All arithmetic and all validations use only the Python standard library.
"""
import argparse

# A signed permutation is stored as signed, one-based column indices, one per row.
I = (1, 2)
ROT = (-2, 1)
REF = (1, -2)


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    return tuple(b[x-1] if x > 0 else -b[-x-1] for x in a)


def trans(a):
    out = [0]*len(a)
    for row, x in enumerate(a, 1):
        out[abs(x)-1] = row if x > 0 else -row
    return tuple(out)


def tensor(a, b):
    return tuple((1 if x*y > 0 else -1)*((abs(x)-1)*len(b)+abs(y)) for x in a for y in b)


J = tensor(REF, REF)
# Kamali and Kharaghani, pp. 141–142. In the printed DGS list, underlining negates an entry.
D7 = ([I, I, I, I, neg(I), neg(I), I], [REF, I, ROT, neg(ROT), ROT, I, neg(REF)])
# Unit complex numbers are stored as powers of i modulo four.
CG3 = ([0, 0, 2], [0, 1, 0])
CG11 = ([0, 1, 2, 0, 2, 1, 3, 2, 1, 1, 0], [0, 0, 3, 3, 3, 0, 0, 1, 2, 0, 2])
# The full binary pairs are Jedwab–Parker (2009), equations (8), (10), (11).
BINARY_SEEDS = {
    2: ("++", "+-"),
    10: ("++-+-+--++", "++-+++++--"),
    26: ("++++-++--+-+-+--+-+++--+++", "++++-++--+-+++++-+---++---"),
}


def binary_multiply(real_length, pair, negate=None):
    """Kamali–Kharaghani Lemma 3, with binary selectors (c+d)/2, (c-d)/2."""
    if negate is None:
        negate = lambda x: (x+2) % 4
    c, d = BINARY_SEEDS[real_length]
    a, b = pair
    e, h = [], []
    for j in range(real_length):
        x, y = c[j], d[j]
        source = a if x == y else b
        if x == "-":
            e.extend(negate(k) for k in source)
        else:
            e.extend(source)
        x, y = c[-1-j], d[-1-j]
        source = b if x == y else a
        if (x == "-") ^ (x == y):
            h.extend(negate(k) for k in source)
        else:
            h.extend(source)
    return e, h


def product(a, c):
    return [(x+y) % 4 for x in a for y in c]


def reverse_conjugate(a):
    return [(-x) % 4 for x in reversed(a)]


def complex18():
    a, b = CG3
    c, d = CG3
    return (product(a,c) + product(b,d),
            product(a,reverse_conjugate(d)) + [(x+2) % 4 for x in product(b,reverse_conjugate(c))])


def verify_complex(pair):
    # Evaluate the aperiodic Laurent identities at a digit base exceeding every coefficient.
    a, b = pair
    n = len(a)
    assert len(b) == n
    base = 1 << (4*n+1).bit_length()
    def evaluate(seq):
        real = imag = 0
        for x in reversed(seq):
            real = base*real + (1, 0, -1, 0)[x]
            imag = base*imag + (0, 1, 0, -1)[x]
        return real, imag
    R = T = 0
    for seq in (a,b):
        u,v = evaluate(seq)
        x,y = evaluate(reverse_conjugate(seq))
        R += u*x-v*y
        T += u*y+v*x
    assert R == 2*n*base**(n-1) and T == 0


def verify_dihedral(pair):
    """Compute every coefficient of all six star commutators and the aperiodic norm."""
    a, b = pair
    first = [(j,v) for j,v in enumerate(a)]
    second = [(j,v) for j,v in enumerate(b)]
    astar = [(-j,trans(v)) for j,v in first]
    bstar = [(-j,trans(v)) for j,v in second]
    def convolution(left,right):
        result = {}
        for e,x in left:
            for f,y in right:
                coeff = result.setdefault(e+f,[0]*4)
                for i,v in enumerate(mul(x,y)):
                    coeff[2*i+abs(v)-1] += 1 if v>0 else -1
        return result
    polynomials = (first, second, astar, bstar)
    for i,x in enumerate(polynomials):
        for y in polynomials[:i]:
            assert convolution(x,y) == convolution(y,x)
    u = convolution(first,astar)
    v = convolution(second,bstar)
    for lag,coeff in u.items():
        total = [x+y for x,y in zip(coeff,v[lag])]
        assert total == ([2*len(a),0,0,2*len(a)] if lag==0 else [0]*4)


def complex_pair(order):
    if order == 25072:
        pair, multipliers = CG3, (2,10,26)
    elif order == 46192:
        pair, multipliers = complex18(), (2,2,2,2,10)
    elif order == 47968:
        pair, multipliers = CG11, (2,)*8
    elif order == 160:                            # full dense positive control, n = 7+3
        pair, multipliers = CG3, ()
    else:
        raise ValueError("supported orders are 160, 25072, 46192, and 47968")
    verify_complex(pair)
    for r in multipliers:
        pair = binary_multiply(r, pair)
        verify_complex(pair)
    return pair


# Craigen–Goethals–Seidel pattern of Kamali–Kharaghani, Lemma 2.
# The second flag means that the source circulant is adjointed before the reflector.
ARRAY = [[(1,0),(-2,0),(-3,0),(-4,0)],[(2,0),(1,0),(-4,1),(3,1)],
         [(3,0),(4,1),(1,0),(-2,1)],[(4,0),(-3,1),(2,1),(1,0)]]


class Matrix:
    def __init__(self, order):
        c,d = complex_pair(order)
        dihedral = binary_multiply(26, D7, neg) if order == 47968 else D7
        a,b = ([tensor(z,I) for z in seq] for seq in dihedral)
        phases = [tensor(I,u) for u in (I,ROT,neg(I),neg(ROT))]
        c,d = ([phases[k] for k in seq] for seq in (c,d))
        self.words = [a+c, a+[neg(x) for x in c], b+d, b+[neg(x) for x in d]]
        self.n = len(self.words[0])
        self.order = order
        assert self.n * 16 == order
        self.blocks = []
        for r in range(4):
            blocks = []
            for j in range(4):
                label, adjoint = ARRAY[r][j]
                seq = self.words[abs(label)-1]
                if adjoint:
                    seq = [trans(seq[-k % self.n]) for k in range(self.n)]
                if r != j:
                    seq = [mul(x,J) for x in seq]
                if label < 0:
                    seq = [neg(x) for x in seq]
                blocks.append(seq)
            self.blocks.append(blocks)

    def entry(self, row, col):
        if not (0 <= row < self.order and 0 <= col < self.order):
            raise IndexError("row or column outside matrix")
        r, x = divmod(row//4, self.n)
        j, y = divmod(col//4, self.n)
        k = (y-x if r == j else -x-y) % self.n
        v = self.blocks[r][j][k][row%4]
        # Right multiply each signed permutation by Sylvester H(4).
        parity = ((abs(v)-1) & (col%4)) in (1,2)
        return (-1 if v < 0 else 1) * (-1 if parity else 1)

    def verify_gram(self):
        # Each block acts as L(z) R^e, R reflecting the n positions; L has 4x4 coefficients.
        # Integer packing in the quotient z^n=1 computes exact circular convolution.
        n = self.n
        bits = (16*n+1).bit_length()
        modulus = (1 << (bits*n)) - 1
        def packed(seq):
            entries = [[0]*4 for _ in range(4)]
            for coeff in reversed(seq):
                for i,v in enumerate(coeff):
                    row = entries[i]
                    for j in range(4):
                        row[j] <<= bits
                    row[abs(v)-1] += 1 if v > 0 else -1
            return [[x % modulus for x in row] for row in entries]
        forward = [[packed(seq) for seq in row] for row in self.blocks]
        reverse = [[packed([seq[0]] + seq[:0:-1]) for seq in row] for row in self.blocks]
        for r in range(4):
            for s in range(r,4):
                for twist in (0,1):
                    terms = [k for k in range(4) if ((r!=k) ^ (s!=k)) == twist]
                    for i in range(4):
                        for j in range(4):
                            total = 0
                            for k in terms:
                                left = forward[r][k][i]
                                right = (forward if twist else reverse)[s][k][j]
                                total += sum(x*y for x,y in zip(left,right))
                            expect = 4*n if r == s and i == j and not twist else 0
                            assert (total-expect) % modulus == 0
        # All signed convolution coefficients including the diagonal subtraction are < 8n+1
        # in magnitude; a nonzero reduced polynomial cannot vanish mod base^n-1.
        return True


def check():
    verify_dihedral(D7)
    verify_dihedral(binary_multiply(26, D7, neg))
    for length, words in BINARY_SEEDS.items():
        assert all(len(w) == length for w in words)
        verify_complex(tuple([0 if c=="+" else 2 for c in w] for w in words))
    for order in (160,25072,46192,47968):
        matrix = Matrix(order)
        assert matrix.verify_gram()
        if order == 160:
            rows = [[matrix.entry(i,j) for j in range(order)] for i in range(order)]
            for i, row in enumerate(rows):
                for j in range(i+1):
                    assert sum(x*y for x,y in zip(row,rows[j])) == (order if i==j else 0)
            # A wrong sign in a genuine monomial coefficient must break the compressed test.
            saved = matrix.blocks[0][1][0]
            matrix.blocks[0][1][0] = neg(saved)
            try:
                matrix.verify_gram()
            except AssertionError:
                pass
            else:
                raise ValueError("the altered-coefficient negative control passed")
        else:
            # Exercise the independent scalar addressing path across every column.
            for i,j in ((0,order//3),(order-1,order//2+3),(7,13)):
                assert sum(matrix.entry(i,k)*matrix.entry(j,k) for k in range(order)) == 0
        print("order",order,"full exact Gram verified", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("coordinates", nargs="*", type=int)
    args = parser.parse_args()
    if args.check and not args.coordinates:
        check()
    elif not args.check and len(args.coordinates)==3:
        order,row,col=args.coordinates
        print(Matrix(order).entry(row,col))
    else:
        parser.error("give --check or ORDER ROW COLUMN")
