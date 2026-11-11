class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for string in s:
            if string == "[" or string == "(" or string == "{":
                arr.append(string)
            elif string == "]":
                if len(arr) > 0:
                    if arr[-1] == "[":
                        arr.pop()
                    else:
                        return False
                else:
                    return False
            elif string == ")":
                if len(arr) > 0:
                    if arr[-1] == "(":
                        arr.pop()
                    else:
                        return False
                else:
                    return False
            elif string == "}":
                if len(arr) > 0:
                    if arr[-1] == "{":
                        arr.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(arr):
            return False
        else:
            return True
        
        