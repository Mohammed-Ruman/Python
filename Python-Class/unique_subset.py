# 3) Write a Python class to get all possible unique subsets from a set of distinct integers 
class SubsetGenerator:
    def __init__(self):
        pass

    def get_subsets(self, nums):
        def backtrack(start, path):
            if len(path) <= len(nums):
                subsets.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        subsets = []
        backtrack(0, [])
        return subsets

# Example usage
generator = SubsetGenerator()
print(generator.get_subsets([4, 5, 6]))
