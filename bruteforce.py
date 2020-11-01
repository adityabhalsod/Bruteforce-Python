# Author
# AdityaBhalsod
# https://github.com/AdityaBhalsod
# It's bruteforce-example using python for generate text

import itertools
import time


class BruteForce(object):
    """
    It's bruteforce generate text class
    """
    MIN_LENGTH = 8
    MAX_LENGTH = 8

    def __init__(self, min_length=MIN_LENGTH, max_length=MAX_LENGTH):
        self.generate(min_length, max_length)

    # more efficent and low memory use for this method
    def grouper(self, iterable, fillvalue=None):
        args = [iter(iterable)]
        return itertools.zip_longest(*args, fillvalue=fillvalue)

    # file write method
    def filewrite(self, product):
        chunks_gen = self.grouper(product)
        for x in chunks_gen:
            file = open(x[0][0] + ".csv", "a")
            file.writelines(("".join(item) + "\n" for item in x if item))
            file.close()

    # BruteForce generate text
    def generate(self, min_length=8, max_length=8):
        # All Character
        # character = "ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        # symbol = """~`!@#$%^&*()[]<>?/,.:;'"-_=+{}|"""
        # number = "0123456789"

        start_time = time.time()  # count time
        for i in range(min_length, max_length + 1):
            product = itertools.product(
                "ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnopqrstuvwxyz", repeat=i
            )
            self.filewrite(product)  # file writeing method
        print(
            "\n\n-----execution time is %s in seconds-----" % (time.time() - start_time)
        )  # print execution time
        return True


if __name__ == "__main__":
    BruteForce()

# Very long time program it's execution
# Very large size file
# Execution time depends your processor
# Example :
# AAAAAAAA
# BAAAAAAA
# CAAAAAAA
# ABAAAAAA
# BBAAAAAA
# CBAAAAAA
# ACAAAAAA
# BCAAAAAA
# CCAAAAAA
# ....(so on)
# CCCCCCCCCC