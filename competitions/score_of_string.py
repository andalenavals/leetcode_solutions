def scoreOfString(s):
    osum=0
    for i in range(len(s)-1):
        osum+=abs( ord(s[i])-ord(s[i+1]) )
    return osum

def tests():
    assert scoreOfString("hello")==13
    assert scoreOfString("zaz")==50

#print(scoreOfString("hello"))
tests()

print(scoreOfString("hello"))
