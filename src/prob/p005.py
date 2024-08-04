class P005:
    def _gcd(self, x, y):
        """
        Calculates the greatest common divisor (GCD) of `x` and `y` using the
        Euclidean algorithm

        For `x` = 12 and `y` = 32, the function returns 4.

        Parameters
        ----------
        num : int
            A positive integer.
        upto : int
            A positive integer.

        Returns
        -------
        int
            The GCD of `x` and `y`.
        """
        while y != 0:
            t = y
            y = x % y
            x = t
        return x

    def aop(self):
        """
        Solves Problem 005 from Project Euler.

        Returns
        -------
        int
            The smallest positive number that is evenly divisible with no
            remainder by all of the numbers from 1 to 20.
        """
        lcm = 1
        num = 1

        while num <= 20:
            lcm = (lcm * num) // self._gcd(lcm, num)
            num += 1

        return lcm


if __name__ == "__main__":
    p = P005()
    print(p.aop())
