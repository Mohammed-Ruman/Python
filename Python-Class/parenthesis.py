class BracketValidator:
    def __init__(self):
        self.opening_brackets = "([{"
        self.closing_brackets = ")]}"
        self.matching_brackets = {")": "(", "]": "[", "}": "{"}

    def is_valid(self, s):
        stack = []
        for char in s:
            if char in self.opening_brackets:
                stack.append(char)
            elif char in self.closing_brackets:
                if not stack or stack.pop() != self.matching_brackets[char]:
                    return False
        return not stack


validator = BracketValidator()
print(validator.is_valid("()"))       
print(validator.is_valid("()[]{}"))   
print(validator.is_valid("[)"))       
print(validator.is_valid("({[)]"))    
print(validator.is_valid("{{{"))      
