class P003:
    def _sf(self, num):
        """
        Returns the smallest factor of `num` using an iterative approach.

        For `num` = 21, the function returns 7.

        Parameters
        ----------
        num : int
            The smallest factor of this number is computed.

        Returns
        -------
        int
            The smallest factor of `num`.
        """
        i = 2
        while num % i != 0:
            i += 1
        return i

    def aop(self):
        """
        Solves Problem 003 from Project Euler.

        Returns
        -------
        int
            The largest prime factor of the number 600851475143.
        """
        num = 600_851_475_143
        prime = self._sf(num)

        while num != 1:
            prime = self._sf(num)
            num //= prime

        return prime


if __name__ == "__main__":
    p = P003()
    print(p.aop())
