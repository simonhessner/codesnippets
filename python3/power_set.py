#!/usr/bin/python3

def get_subsets(fullset):
    n = len(fullset)
    return [[fullset[k] for k in range(n) if i&1<<k] for i in range(2**n)]

testsets = [[], [1], [1,2], [1,2,3]]
for testset in testsets:
	subsets = get_subsets(testset)
	print(testset, "->", len(subsets), subsets)