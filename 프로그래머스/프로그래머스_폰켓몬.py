def solution(nums):
    can = int(len(nums) / 2)

    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1

    kind = len(dic.keys())

    if kind < can:
        return (kind)
    else:
        return (can)