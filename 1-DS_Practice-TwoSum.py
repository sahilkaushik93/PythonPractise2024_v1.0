# BRUTE FORCE --> O(n^2)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        twoSumOutputLst = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if i == j:
                        pass
                    else:
                        print("i: ",nums[i])
                        print("j: ",nums[j])
                        print(f"target: {target}")
                        twoSumOutputLst.append(i)
                        twoSumOutputLst.append(j)
                        twoSumOutputLst = list(set(twoSumOutputLst))

        return twoSumOutputLst


test = Solution()
test1 = test.twoSum([3,2,4], 6)
print(test1)

# Hash Table --> O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        match_hash = {}

        for i in range(len(nums)):
            print(match_hash)
            if nums[i] in match_hash:
                return [match_hash[nums[i]], i]
            else:
                match_hash[target-nums[i]] = i

test = Solution()
test1 = test.twoSum([3,2,4], 6)
print(test1)
