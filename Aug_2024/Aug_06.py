class Solution:
    def isValid(self, a):
        c = a.split('.')
        if len(c) != 4:
            return False
        for b in c:
            if b and ((len(b) > 1 and b[0] != '0') or len(b) == 1 ):
                if not (int(b) >=0 and int(b) <= 255):
                    return False
                    break
            else:
                return False
        return True