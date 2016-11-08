# task1
def find_value_in_matrix(P, N, M):
    return int(M*P + N + (1-M)*M/2)


# task2
def find_amount_of_ways_in_square(n=20):
    def fact(n):
        if n in (0, 1):
            return 1
        return n*fact(n-1)

    return fact(2*n) / (fact(n/2))**2

if __name__ == '__main__':
    print find_amount_of_ways_in_square()
