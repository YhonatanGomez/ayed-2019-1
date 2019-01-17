import json

def rev(text,cv,cc,cont,voc):
    if cont==len(text):
        if cv>cc:
            return True
        elif cv<cc or cc==cv:
            return False
    else:
        for i in range(len(voc)):
            if text[cont]==voc[i]:
                cv=cv+1
            if i==4:
                if text[cont]!="a" and text[cont]!="e" and text[cont]!="i" and text[cont]!="o" and text[cont]!="u":
                    cc=cc+1
        return rev(text,cv,cc,cont+1,voc)
                
# TODO Complete!
def has_more_vowels(s):
    s=s.lower()
    voc=["a","e","i","o","u"]
    c=rev(s,0,0,0,voc)
    return c


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
