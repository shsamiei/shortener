import string
from .models import Shortener
from .singleton import singleton

#TODO : make it singlton class 

@singleton
class ShortenerService:

    prime_numbers = [65423, 66721, 73517, 78697, 86249, 95923, 50591, 20663, 22739, 101141]
    max_length = 2000
    mod_base = 64 ** 8
    bases = []
    digs = string.digits + string.ascii_letters + '-_'


    def __init__(self) -> None:
        self.generate_bases()

    
    @classmethod
    def long_to_short_url(cls, url):
        base = 0 
        url_base64 = cls._int2base(cls.sum_of_ord(url))
        if Shortener.objects.filter(shortener=url_base64, url=url).exists():
            return Shortener.objects.filter(shortener=url_base64, url=url).first().shortener

        has_collision = Shortener.objects.filter(shortener=url_base64).exists()

        while has_collision : 
            base += 1
            url_base64 = cls._int2base(cls.sum_of_ord(url=url, base=base))
            has_collision = Shortener.objects.filter(shortener=url_base64).exists()

        return url_base64


    @classmethod
    def get_url(cls, shortener_url):

        shortener_link = 'http://127.0.0.1:8000/'+ shortener_url
        obj = Shortener.objects.filter(shortener=shortener_link)

        if obj.exists():
            obj.first().clicks_increament()
            return obj.first().url
        return None


    @classmethod
    def generate_bases(cls):
        for prime in cls.prime_numbers: 
            cls.bases.append([prime])
        for base in cls.bases:
            for i in range(1, cls.max_length):
                base.append(base[0] * base[i-1])



    @classmethod
    def sum_of_ord(cls, long_url, base=0):
        return sum([(ord(x) * cls.bases[base][it]) % cls.mod_base for it, x in enumerate(long_url)]) % cls.mod_base


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

    