from complexNumber import ComplexNumber

if __name__ == '__main__':
    c1 = ComplexNumber(real = 3, imaginary = 4)
    c2 = ComplexNumber(real = 4, imaginary = 5)
    c3 = c1 / c2
    print(c3)
    # print(c.conjugate())