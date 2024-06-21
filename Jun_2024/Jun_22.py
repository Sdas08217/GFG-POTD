# Extract the Number from the String
class Solution:
    def ExtractNumber(self, sentence):
        numbers = []
        current_number = ''
        
        # Step 1: Iterate through the sentence to extract numbers
        for char in sentence:
            if char.isdigit():
                current_number += char
            else:
                if current_number:
                    numbers.append(current_number)
                    current_number = ''
        
        # Append the last number if the sentence ends with a digit
        if current_number:
            numbers.append(current_number)
        
        # Step 2: Filter out numbers containing '9'
        valid_numbers = [int(num) for num in numbers if '9' not in num]
        
        # Step 3: If there are no valid numbers, return -1
        if not valid_numbers:
            return -1
        
        # Step 4: Return the largest number from the valid numbers
        return max(valid_numbers)

# Example usage
solution = Solution()
print(solution.ExtractNumber("This is alpha 5057 and 97"))  # Output: 5057
print(solution.ExtractNumber("Another input 9007"))         # Output: -1
print(solution.ExtractNumber("This has 89 and 12345678 and 123456780"))  # Output: 123456780
