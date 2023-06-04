import random

def rand_cccd(size):
    cccd = set()

    while len(cccd) != size:
        num = ''.join(str(random.randint(0, 9)) for _ in range(12))
        cccd.add(num)
    return cccd

import time
# start_time = time.time()
# random_numbers = rand_cccd(1000000)
#
# end_time = time.time()
#
# runtime = end_time - start_time
# print("Runtime:", runtime, "seconds")