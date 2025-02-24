import math
import scipy.special
from fractions import Fraction
from tabulate import tabulate

# For all functions, we use
# n = total population
# t = number of corruptions in total population
# k = security parameter
# s = committee size
# h = minimum number of honest parties required in committee
# p_max = maximal value for which pFail returns correct value. Output is 1 if p_fail > p_max.

def p_fail(n, t, s, h, p_max):
    p = 0
    # Compute n choose s as exact integer
    denom = scipy.special.comb(n, s, exact=True)
    for i in range(s - h + 1, s + 1):
        p += Fraction(scipy.special.comb(t, i, exact=True) * scipy.special.comb(n - t, s - i, exact=True), denom)
    if p > p_max:
        return 1
    return p

# Minimum committee size with corruption ratio at most cr such that p_fail <= 2^{-k}
def min_csize(n, t, cr, k):
    p_max = Fraction(1, 2 ** k)
    for s in range(1, n + 1):
        # We want at least h honest parties
        h = math.ceil((1 - cr) * s)
        if p_fail(n, t, s, h, p_max) <= p_max:
            return s

# Compute analytical upper bound
def analytic_bound(p, cr, k):
    q = cr
    alpha = q - p
    beta = (math.e * math.sqrt(q) * (1 - p)) / (2 * math.pi * alpha * math.sqrt(1 - q))
    bound = math.ceil(k / math.log((q / p) ** q * ((1 - q) / (1 - p)) ** (1 - q), 2))
    beta_bound = math.ceil(beta * beta)
    return max(bound, beta_bound)

# Print committee sizes for different parameters
def print_csizes(ns, ps, k, crs):
    header = ["", ""] + [float(cr) for cr in crs]
    table = []
    for p in ps:
        table.append(["analytic", "p = " + str(p)] + [analytic_bound(p, cr, k) for cr in crs])
        for n in ns:
            t = n * p
            table.append(["n = " + str(n), "p = " + str(p)] + [min_csize(n, t, cr, k) for cr in crs])
    print(tabulate(table, header))

# Print coordinates of committee sizes over guaranteed honesty
def print_graph_coordinates(n, t, k):
    for crp in range(99, 32, -1):  # Corruption from 99% down to 33%
        cr = Fraction(crp, 100)  # Convert percentage to fraction
        print(f"({100 - 100 * cr},{min_csize(n, t, cr, k)})", end=' ')
    print("\n")

# Print analytic bound for coordinates of committee sizes over guaranteed honesty
def print_analytic_graph_coordinates(p, k):
    for crp in range(99, 32, -1):  # Corruption from 99% down to 33%
        cr = Fraction(crp, 100)  # Convert percentage to fraction
        print(f"({100 - 100 * cr},{analytic_bound(p, cr, k)})", end=' ')
    print("\n")

def main():
    # Consider total populations 10000 and 2000 with 30% and 20% corruption, with 60-bit security
    print("Main function is running...")

    ns = [1000, 200] #[10000, 2000]
    ps = [Fraction(3, 10), Fraction(2, 10)]
    k = 60
    # Maximal corruption ratios in committees from 99% to 33%
    crs = [
        Fraction(99, 100), Fraction(89, 100), Fraction(79, 100), Fraction(69, 100),
        Fraction(59, 100), Fraction(49, 100), Fraction(39, 100), Fraction(1, 3)
    ]
    # Print table with committee sizes
    print_csizes(ns, ps, k, crs)
    print("\n")
    # Print graph coordinates
    for p in ps:
        print(f"Analytic graph coordinates, p = {p}, k = {k}")
        print_analytic_graph_coordinates(p, k)
        for n in ns:
            print(f"Graph coordinates, n = {n}, p = {p}, k = {k}")
            t = n * p
            print_graph_coordinates(n, t, k)

if __name__ == '__main__':
    main()

    # hello