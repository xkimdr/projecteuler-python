class P007:
    def _isp(self, num):
        """
        Checks whether the given `num` is a prime number.

        For `num` = 3, the function returns `True`.

        Parameters
        ----------
        num : int
            The number to be checked for primality.

        Returns
        -------
        bool
            `True` if `num` is a prime number, otherwise `False`.
        """
        if num <= 1:
            return False
        elif num == 2 or num == 3:
            return True
        else:
            i = 2

            while i * i <= num:
                if num % i == 0:
                    return False
                i += 1

            return True

    def aop(self):
        """
        Solves Problem 007 from Project Euler.

        Returns
        -------
        int
            The 10,001st prime number.
        """
        count = 0
        i = 2

        while count < 10_001:

            if self._isp(i):
                count += 1
            i += 1

        i -= 1
        return i


if __name__ == "__main__":
    p = P007()
    print(p.aop())
