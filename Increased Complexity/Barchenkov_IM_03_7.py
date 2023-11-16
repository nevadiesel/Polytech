'''
The numbers 12, 63 and 119 have something in common related with their divisors and their prime factors, let's see it.
Numbers PrimeFactorsSum(pfs)        DivisorsSum(ds)              Is ds divisible by pfs
12         2 + 2 + 3 = 7         1 + 2 + 3 + 4 + 6 + 12 = 28            28 / 7 = 4,  Yes
63         3 + 3 + 7 = 13        1 + 3 + 7 + 9 + 21 + 63 = 104         104 / 13 = 8, Yes
119        7 + 17 = 24           1 + 7 + 17 + 119 = 144                144 / 24 = 6, Yes
There is an obvius property you can see: the sum of the divisors of a number is divisible by the sum of its prime factors.

We need the function ds_multof_pfs() that receives two arguments: nMin and nMax, as a lower and upper limit (inclusives),
respectively, and outputs a sorted list with the numbers that fulfill the property described above.

We represent the features of the described function:
ds_multof_pfs(nMin, nMax) -----> [n1, n2, ....., nl] # nMin ≤ n1 < n2 < ..< nl ≤ nMax

Let's see some cases:
ds_multof_pfs(10, 100) == [12, 15, 35, 42, 60, 63, 66, 68, 84, 90, 95]
ds_multof_pfs(20, 120) == [35, 42, 60, 63, 66, 68, 84, 90, 95, 110, 114, 119]
Enjoy it!!
'''

from array import array

# Решето Эратосфена для нахождения простых множителей для всех чисел до n


def sieve_of_eratosthenes(n: int) -> array:
    spf = array('I', [i for i in range(n + 1)])
    spf[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

# Поиск чисел между nMin и nMax, сумма делителей которых делится на сумму их простых множителей.


def ds_multof_pfs(nMin, nMax):
    spf = sieve_of_eratosthenes(nMax)
    result = []
    for n in range(nMin, nMax + 1):
        # Сумма простых множителей
        tmp_n, pfs = n, 0
        while tmp_n > 1:
            pfs += spf[tmp_n]
            tmp_n //= spf[tmp_n]

            # Сумма делителей
        tmp_n, ds = n, 1
        while tmp_n > 1:
            p = spf[tmp_n]
            term = 1
            while tmp_n % p == 0:
                tmp_n //= p
                term = term * p + 1
            ds *= term

        if ds % pfs == 0:
            result.append(n)
    return result


print(ds_multof_pfs(10, 100))
print(ds_multof_pfs(20, 120))
