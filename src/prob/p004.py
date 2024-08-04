class P004:
    def _isp(self, num):
        """
        Determines whether the given `num` is a palindrome.

        For `num` = 121, the function returns `True`.

        Parameters
        ----------
        num : int
            The number to be checked for palindromicity.

        Returns
        -------
        bool
            `True` if `num` is a palindrome, otherwise `False`.
        """
        xy = num
        yx = 0

        while num != 0:
            yx = yx * 10 + num % 10
            num //= 10

        return xy == yx

    def aop(self):
        """
        Solves Problem 004 from Project Euler.

        Returns
        -------
        int
            The largest palindrome made from the product of two 3-digit
            numbers.
        """
        palindrome = 0

        for i in range(999, 99, -1):
            for j in range(90, 9, -1):
                product = 11 * i * j
                if product > palindrome and self._isp(product):
                    palindrome = product

        return palindrome


if __name__ == "__main__":
    p = P004()
    print(p.aop())
