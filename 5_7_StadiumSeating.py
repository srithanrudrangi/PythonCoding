classA = int(input('How many tickets are sold for class A ?'))
classB = int(input('How many tickets are sold for class B ?'))
classC = int(input('How many tickets are sold for class C ?'))


def formulas():
    classAincome = classA*20
    classBincome = classB*15
    classCincome = classC*10


formulas(classAincome + classBincome + classCincome)
