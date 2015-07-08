class Solution:
# @param {integer} n
# @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and n & n-1 == 0


if __name__ == "__main__":
    S = Solution()
    f = S.isPowerOfTwo
    goodTenValues = [2**i for i in range(10)]
    badTenValues = [3**i for i in range(1,11)]
    res = map(f, goodTenValues + badTenValues)
    assert all(res[:10])
    assert not any(res[10:])
