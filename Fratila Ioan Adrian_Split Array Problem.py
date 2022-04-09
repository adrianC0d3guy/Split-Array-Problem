# I did not understand exactly if the list will be empty, what will be the result so
# supposed that if the list will be empty, than the result will be False;
from typing import List


# Function splitArraySameAverage(list) is supposed to return True if the initial list can be splitted into two
# sub-lists, such that the average of the elements situated within the sub-lists is equal.
# EXAMPLE: A = [1, 2, 3, 4, 5, 6, 7, 8] -> OUTPUT : True
# EXPLANATION: B = [1, 4, 5, 8] and C = [2, 3, 6, 7]
def splitArraySameAverage(A: List[int]) -> bool:
    # A subfunction that see if total k elements sums to target
    # target is the goal, k is the number of elements in set B, i is the index we have traversed through so far
    mem = {}

    def find(target, k, i):
        # if we are down searching for k elements in the array, see if the target is 0 or not. This is a basecase
        if k == 0: return target == 0

        # if the to-be selected elements in B (k) + elements we have traversed so far is larger than total length of A
        # even if we choose all elements, we don't have enough elements left, there should be no valid answer.
        if k + i > len(A): return False

        if (target, k, i) in mem: return mem[(target, k, i)]

        # if we choose the ith element, the target becomes target - A[i] for total sum
        # if we don't choose the ith element, the target doesn't change
        mem[(target - A[i], k - 1, i + 1)] = find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)

        return mem[(target - A[i], k - 1, i + 1)]

    n, s = len(A), sum(A)
    # Observation: the smaller set has length j ranging from 1 to n//2 + 1
    # we iterate for each possible length j of array B from length 1 to length n//2 + 1
    # if s*j%n, which is the sum of the subset, it should be an integer, so we only proceed to check if s * j % n == 0
    # we check if we can find target sum s*j//n (total sum of j elements that sums to s*j//n)
    return any(find(s * j // n, j, 0) for j in range(1, n // 2 + 1) if s * j % n == 0)


# Function alwaysTrueOtherElements(list) is supposed to check if the elements within the initial
# list are all equal and it will return True if they are indeed equal;
# This check was made because it has no sense to compute the splitArraySameAverage(list)
# function in the case where explained two rows above.
def alwaysTrueElements(A: List[int]) -> bool:
    for i in range(len(A)):
        if A[i] == A[i + 1]: return True


# Function alwaysFalse(list) is supposed to check if there is only one
# element in the list and it will return False if there is indeed only one element;
# This check was made because it has no sense to compute the splitArraySameAverage(list)
# function in the case where explained two rows above.
def alwaysFalse(A: List[int]) -> bool:
    if len(A) == 1: return False


# Function indexError(list) is supposed to raise index errors, because A should be in range [1, 30]
# and A[i] should be in range [0, 10000].
def indexError(A: List[int]):
    for i in range(1, len(A)):
        if A[i] < 0 or A[i] > 10000:
            raise IndexError("ERROR: The elements within the list should be greater or equal to 0 and lesser or equal "
                  "to 10000!")
        elif len(A) > 30:
            raise IndexError("ERROR: Range of the list is [1, 30]; Your index should be lesser or equal to 30!")


# Function test_functions() it was made only for good optimization, which means that before
# appealing the main functions, I will test each and every one of them to see if they are working properly;
# The program should raise errors if the tests are not passed
def testFunctions():
    assert splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 9]) == False
    assert alwaysTrueElements([0, 0, 0, 0, 0]) == True
    assert alwaysTrueElements([1, 1, 1, 1, 1]) == True
    assert alwaysTrueElements([20, 20, 20, 20, 20]) == True
    assert alwaysFalse([2]) == False
    assert alwaysFalse([9999]) == False
    assert alwaysFalse([0]) == False


if __name__ == '__main__':
    #listA = [1, 2, 3, 4, 5, 6, 7, 8]
    listA = []

    # Number of elements as input. Be aware, the range of the list will be [1, 30]
    n = int(input("Enter number of elements : "))

    # Iterating till the range
    for i in range(1, n):
        ele = int(input("listA[" + str(i) + "] = "))

        listA.append(ele)  # Adding the element in the list

    testFunctions()
    print("Every function has passed the testFunction!")
    if not alwaysFalse(listA) or alwaysTrueElements(listA): print(splitArraySameAverage(listA))

