class P002:
    def aop(self):
        """
        Solves Problem 002 from Project Euler.

        Returns
        -------
        int
            The sum of the even-valued terms of Fibonacci sequence whose values
            do not exceed 4 million.
        """
        previous = 2
        current = 8
        next = previous + 4 * current
        sum = previous + current

        while next <= 4_000_000:
            sum += next
            previous = current
            current = next
            next = previous + 4 * current

        return sum


if __name__ == "__main__":
    p = P002()
    print(p.aop())
