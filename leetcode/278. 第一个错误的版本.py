# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid - 1) and isBadVersion(mid):
                return mid
            elif isBadVersion(mid + 1) and not isBadVersion(mid):
                return mid + 1
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1


class Solution1:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
