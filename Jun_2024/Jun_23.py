# Print Bracket Number
class Solution:
	def bracketNumbers(self, str):
	    stack = [] 
	    c = 0
	    ans = []
	    for i in range(len(str)):
	        if(str[i] == '('):
	            c += 1 
	            ans.append(c)
	            stack.append(c)
	        elif(str[i] == ')'):
	            ans.append(stack[-1]) 
	            stack.pop() 
	    return ans

# Example usage
solution = Solution()
input_string = "(a+(b*c))+(d/e)"
result = solution.bracketNumbers(input_string)
print(f"Input: {input_string}")
print(f"Bracket Numbers: {result}")
