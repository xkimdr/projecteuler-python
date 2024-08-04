class P001:
    def _som(self, num, upto):
        """
        Calculates the sum of multiples of `num` that are less than `upto + 1`.

        For `num` = 3 and `upto` = 10, the function returns the sum of 3, 6,
        and 9, totaling 18.

        Parameters
        ----------
        num : int
            The function sums multiples of this positive integer.
        upto : int
            Only multiples less than or equal to this value are summed.

        Returns
        -------
        int
            The sum of all multiples of `num` that are less than or equal to
            `upto`.
        """
        count = upto // num
        return num * count * (count + 1) // 2

    def aop(self):
        """
        Solves Problem 001 from Project Euler.

        Returns
        -------
        int
            The sum of all multiples of 3 or 5 below 1000.
        """
        return self._som(3, 999) + self._som(5, 999) - self._som(15, 999)


if __name__ == "__main__":
    p = P001()
    print(p.aop())
