# https://leetcode.com/problems/reorder-data-in-log-files/

# time complexity: O(nlog(n))

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda log: ((l:= log.split())[1:], l[0]))
        return letters + digits