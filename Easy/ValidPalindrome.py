class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Remove non-alphanumeric characters and normalize case
        filteredString = ''.join(char.lower() for char in s if char.isalnum())
        
        # Step 2: Check if the cleaned string is equal to its reverse
        return filteredString == filteredString[::-1]