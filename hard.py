from collections import deque

def max_sliding_window(nums, k):
    if not nums:
        return []

    if k == 0:
        return nums

    deq = deque()
    result = []

    for i in range(len(nums)):
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            result.append(nums[deq[0]])

    return result


def convert_to_int_list(input_str):
    return [int(x) for x in input_str.split(',')]


input_nums = input("nums = ")
nums = convert_to_int_list(input_nums)
k = int(input("k= "))

print( max_sliding_window(nums, k))
