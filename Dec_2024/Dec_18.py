class Solution:
    def isValid(self, arr, n, k, maxPages):
        students = 1
        current_pages = 0
        
        for pages in arr:
            if pages > maxPages:
                return False  # A single book has more pages than maxPages, not possible
            
            if current_pages + pages > maxPages:
                students += 1
                current_pages = pages
                
                if students > k:
                    return False
            else:
                current_pages += pages
        
        return True
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:
            return -1  # Not enough books to allocate to each student
        
        low = max(arr)
        high = sum(arr)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.isValid(arr, n, k, mid):
                result = mid
                high = mid - 1  # Try for a smaller maximum
            else:
                low = mid + 1  # Increase the maximum to find a valid solution
        
        return result
