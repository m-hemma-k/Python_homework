#!/usr/bin/env python3

# Three positive integers k m and n representing a population containing k+m+n organisms:
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Output: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). 
# Assume that any two organisms can mate.

def calc_dom(k, m, n):
    s = k + m + n
    dom1 = k/s
    dom2 = m/s * (4*k + 3*m - 3 + 2*n)/(4*(s - 1))
    dom3 = n/s * (2*k + m)/(2*(s - 1))
    tot = dom1 + dom2 + dom3
    return tot

def main():
    print(calc_dom(17, 21, 20)) #17 21 20

if __name__ == '__main__':
    main()