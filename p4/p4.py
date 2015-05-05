def isPalindrome(n):
    nStr = str(n)
    numLen = len(nStr)
    for idx in range(0,numLen/2):
        if (nStr[idx] != nStr[numLen-idx-1]):
            return False
    return True

def runPalindromeTests():
    print isPalindrome(906609)
    print isPalindrome(1001)
    print isPalindrome(101)
    print isPalindrome(11)
    print isPalindrome(1234321)
    print isPalindrome(1)
    print isPalindrome(2131231)

def findLargest():
    products = []
    for idx in reversed(range(100,1000)): # doesn't include 1000
        for jdx in reversed(range(100,1000)): # doesn't include 1000
            if isPalindrome(idx*jdx):
                products.append(idx*jdx)
    return products

palindromes = findLargest()
palindromes.sort()
print palindromes[-1]
