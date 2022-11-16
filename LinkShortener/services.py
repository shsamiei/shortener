class ShortenerService:






    @classmethod
    def _int2base(cls, x, base=64):
        if x < 0:
            sign = -1
        elif x == 0:
            return cls.digs[0]
        else:
            sign = 1

        x *= sign
        digits = []

        while x:
            digits.append(cls.digs[int(x % base)])
            x = int(x / base)

        if sign < 0:
            digits.append('-')

        digits.reverse()

        return ''.join(digits)
