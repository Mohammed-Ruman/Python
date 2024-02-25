class TwoSumFinder:
    def __init__(self):
        pass

    def find_indices(self, numbers, target):
        num_dict = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return None

# Example usage
finder = TwoSumFinder()
numbers = [90, 20, 10, 40, 50, 60, 70]
target = 50
print(finder.find_indices(numbers, target))
