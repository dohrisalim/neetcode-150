class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_representation = bin(n)[2:]

        return binary_representation.count('1')