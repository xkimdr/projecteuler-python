class P006:
    def aop(self):
        """
        Solves Problem 006 from Project Euler.

        Returns
        -------
        int
            The difference between the sum of the squares of the first one
            hundred natural numbers and the square of the sum.
        """
        num = 100
        return (num - 1) * num * (num + 1) * (3 * num + 2) // 12


if __name__ == "__main__":
    p = P006()
    print(p.aop())
