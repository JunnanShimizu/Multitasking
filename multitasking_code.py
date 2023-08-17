# Junnan Shimizu
# Projet 5
# 3/20/22
# CS337

import multiprocessing
import time
from multiprocessing import Pool
import re
from matplotlib import pyplot as plt

data = []
def read_files(file_names):
    time_one = time.perf_counter()
    print("The number of cores in the system is", multiprocessing.cpu_count())
    pool = Pool(processes=8)
    pool.map(read_file, file_names)
    elapsed_time = time.perf_counter() - time_one
    data.append(elapsed_time)
    print('Elapsed Time', elapsed_time)
    plt.title("Times")
    plt.ylabel("Time")
    plt.xlabel("Frequency Time, Common Words Time, Elapsed Time")
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    plt.bar(x, data)
    plt.show()

def read_file(file_name):
    data = []
    time_one = time.perf_counter()
    word_count = 0
    hash_map = dict()
    file = open(file_name)
    for line in file:
        for current in line.split():
            word_count += 1
            current = current.lower()
            word = re.sub(r'[^A-Za-z0-9 ]+', '', current)
            if hash_map.get(word) is None:
                hash_map.update({word: +1})
            else:
                hash_map[word] = hash_map[word] + 1

    print('Frequency of the word: hello,', (hash_map['hello'] / word_count))
    word_trends_total = time.perf_counter() - time_one
    data.append(word_trends_total)
    print('Time to find word frequency', word_trends_total)

    sorted_hash_map = sorted(hash_map.items(), key=lambda kv: kv[1], reverse=True)
    print(file_name)
    for i in range(10):
        print(sorted_hash_map[i])
    common_words_time_total = time.perf_counter() - time_one
    data.append(common_words_time_total)
    print("Time to find 10 most common words:", common_words_time_total)
    print(f"Word Count: {word_count}")

    return sorted_hash_map


