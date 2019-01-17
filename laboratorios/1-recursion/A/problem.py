import json
def gir(text, cont,rev):
    if cont==-1:
        return rev
    else:
        rev=rev+str(text[cont])
        return gir(text,cont-1,rev)
    

# TODO Complete!!
def reverse(text):
    rev=""
    t=gir(text,len(text)-1,rev)
    return t


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
