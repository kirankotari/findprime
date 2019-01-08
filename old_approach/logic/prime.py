from math import sqrt
import time
import os
import json


class Prime1(object):
    primes = []
    primes_time = []
    prime_len = 0

    def __init__(self):
        self.read()

    def check_prime(self, n):
        start = time.time()
        is_prime = True
        r = sqrt(n)
        for d in self.primes:
            if d > r + 1:
                is_prime = False
            if n % d == 0:
                is_prime = False
            if not is_prime:
                n = 0
                break
        return n, time.time() - start

    def add(self, n, t):
        self.primes.append(n)
        t += self.primes_time[-1]
        self.primes_time.append(t)

    def read(self, path=r'../prime/'):
        self.primes = []
        ls = os.listdir(path)
        for each_file in ls:
            with open(path + each_file) as f:
                fdata = json.load(f)
                self.primes += fdata['prime']
                self.primes_time.append(fdata['time'][-1])
        self.prime_len = len(self.primes)

    def write(self, path=r'../prime/'):
        data = {"prime": self.primes[self.prime_len:], "time": self.primes_time[1:]}
        with open("{}{}.json".format(path, self.prime_len), 'w') as f:
            json.dump(data, f)
        self.prime_len = len(self.primes)

    # TODO: When to call check_prime and add
    # TODO: When to write..!


class Github(object):
    pass


class Prime(object):
    primes = []
    ptime = []
    ptdiff = 0
    pre_prime = [1, 2]
    start_range = 3
    end_range = 1000000

    def __init__(self):
        pass

    def find(self, n):
        start = time.time()
        flag = False
        psqrt = sqrt(n)
        for p in self.primes:
            if p > psqrt + 1:
                break
            if n % p == 0:
                flag = True
                break
        diff = (time.time() - start)*1000000000
        if flag is False:
            return n, diff
        return None, diff

    def find_range(self, start_range, end_range):
        if start_range % 2 == 0:
            start_range += 1
        for each in range(start_range, end_range, 2):
            p, t =self.find(each)
            if p:
                self.primes.append(p)
                self.ptdiff += t
                self.ptime.append(self.ptdiff)

    def run(self):
        for i in range(1000):
            t = (self.start_range, self.end_range)
            self.find_range(*t)
            self.start_range = self.end_range
            self.end_range += 1000000
        # print(self.primes)
        # print(self.ptime)

    def run1(self):
        from multiprocessing import Pool
        agents = 10
        chunksize = 1000000
        if self.start_range % 2 == 0:
            self.start_range += 1
        end_range = 1000000000
        with Pool(processes=agents) as pool:
            result = pool.map(self.find, range(self.start_range, end_range, 2), chunksize)
        pass


if __name__ == "__main__":
    p = Prime1()
    print(p.primes)
    print(p.primes_time, p.prime_len)
    # p.run()
