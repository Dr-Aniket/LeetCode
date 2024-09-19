class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Base case: if the expression is a number, return it as a single-element list.
        if expression.isdigit():
            return [int(expression)]
        
        result = []
        
        # Divide the expression into parts using every operator found
        for i, char in enumerate(expression):
            if char in "+-*":
                # Recursively calculate left and right parts
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                # Combine the results of left and right parts using the operator
                for l in left:
                    for r in right:
                        if char == '+':
                            result.append(l + r)
                        elif char == '-':
                            result.append(l - r)
                        elif char == '*':
                            result.append(l * r)
        
        return result