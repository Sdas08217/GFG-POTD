class Solution:    
    def ValidCorner(self, mat): 
        n = len(mat)
        m = len(mat[0])

        # Use a dictionary to track column pairs that have already been seen in a row
        seen_pairs = set()

        for i in range(n):
            ones_in_row = []
            # Collect all columns where the current row has 1
            for j in range(m):
                if mat[i][j] == 1:
                    ones_in_row.append(j)
            
            # Check all pairs among those columns
            for c1 in range(len(ones_in_row)):
                for c2 in range(c1 + 1, len(ones_in_row)):
                    col_pair = (ones_in_row[c1], ones_in_row[c2])
                    if col_pair in seen_pairs:
                        return True
                    seen_pairs.add(col_pair)
        
        return False
