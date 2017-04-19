class PrimeGenerator(object):
    def __init__(self, n):
        self.n = n

    def prime_generator(self):

        """ The Function takes O(N^2)"""
        result = []
        n = self.n
        if isinstance(n, int):
            for x in range(0, n + 1):
                if x < 2:
                    r = 0
                else:
                    i = 2
                    while i < x:
                        if x % i == 0:
                            break
                        i = i + 1
                    else:
                        result.append(x)

        return result

