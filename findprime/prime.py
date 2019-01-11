from os import path
from ThePrime.lib import Lib


class Prime:
    def __init__(self, fname, fpath):
        self.prime_file = fname
        self.path = fpath
        self.data = self._read()
        self.primes = self.data.keys()

    def _read(self):
        return Lib.read_json('{}/{}'.format(self.path, self.prime_file))

    def find(self, start, end):
        main_set = Lib.odd_range(start, end)
        for each_prime in self.primes:
            pm = Lib.multiples(self.data[each_prime], int(each_prime), end)
            self.data[each_prime] = pm[-1]
            main_set -= set(pm)
        return main_set

if __name__ == "__main__":
    file_name = r'10^0-10^1.json'
    file_path = path.abspath(r'../data')
    obj = Prime(file_name, file_path)
    print(obj.primes)
    print(obj.data)
    primes = obj.find(2, 100)
    print(primes)
    print(obj.data)
