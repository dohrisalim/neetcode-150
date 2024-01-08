class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}

        for num in nums:
            if num in temp:
                temp[num] += 1
            else:
                temp[num] =  1

        result = sorted(temp, key=temp.get, reverse=True)


        return result[:k]