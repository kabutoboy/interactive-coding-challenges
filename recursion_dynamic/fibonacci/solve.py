class Math(object):

    def fib_iterative(self, n):
        F_0, F_1, F_n = 0, 1, 0
        for i in range(1, n):
            F_n = F_0 + F_1
            F_0 = F_1
            F_1 = F_n
        return F_n

    def fib_recursive(self, n):
        if n < 2:
            return n
        return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)

    def fib_dynamic(self, n):
        F_0, F_1, F_n = 0, 1, 0
        for i in range(0, n):
            F_n = F_0 + F_1
            F_0 = F_1
            F_1 = F_n
        return F_n
