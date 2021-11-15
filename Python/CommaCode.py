def ExpandList(list):
    sentence = list[0]
    for index, item in enumerate(list):
        if(index == len(list)-1):
            sentence = sentence + ' and ' + item
        elif(index!=0):
            sentence = sentence + ", " + item
    print(sentence)

fruits = ['apples','bananas','tofu','cats','ice cream']
ExpandList(fruits)