import itertools
import time


# more efficent and low memory use for this method
def grouper(iterable,fillvalue=None):
    args = [iter(iterable)]
    return itertools.zip_longest(*args, fillvalue=fillvalue)

# file write method
def filewrite(p):
	chunks_gen = grouper(p)
	for x in chunks_gen:
		fobj=open(x[0][0]+".csv",'a')
		fobj.writelines([''.join(l) + '\n' for l in x if l])
		fobj.close()
		
# main method
def bruteforce(min_len=8,max_len=8):
	test_list = """ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()[]<>?/,.:;'"-_=+{}|""" # All Character	
	start_time = time.time() # count time
	for i in range(8,max_len+1):
		p = itertools.product(test_list, repeat=i)
		filewrite(p) # file writeing method
	print("\n\n-----execution time is %s in seconds-----" % (time.time() - start_time)) # print execution time
	return True



bruteforce(8,32)

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