class Solution:
    def productExceptSelf(self, nums):
        res = []

        for i in range(len(nums)):
            prod = 1

            for j in range(len(nums)):
                if i != j:
                    prod = prod * nums[j]

            res.append(prod)

        return res
       