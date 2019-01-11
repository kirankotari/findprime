import json

class Lib:
    @staticmethod
    def is_even(n):
        n = str(n)
        if n[-1] == '0' or n[-1] == '2' or n[-1] == '4' or n[-1] == '6' or n[-1] == '8':
            return True
        return False

    @staticmethod
    def odd_range(start, end):
        if Lib.is_even(start):
            start += 1
        return set(range(start, end, 2))

    @staticmethod
    def triple(n, m=None):
        if m is None: m = n
        return m + n + n

    @staticmethod
    def multiples(n, m, end):
        result = list()
        while m < end:
            result.append(m)
            m = Lib.triple(n, m)
        return result

    @staticmethod
    def read_json(file):
        with open(file) as fp:
            return json.load(fp)

    @staticmethod
    def write_json(file, data):
        with open(file, 'w') as fp:
            json.dump(data, fp)
