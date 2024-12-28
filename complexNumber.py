class ComplexNumber:
    def __init__(self, real = 0.0, imaginary = 0.0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        string = f"{self.real}" if self.real > 0 else ""
        imaginary = self.imaginary
        imaginary = abs(imaginary)

        if(imaginary == 0):
            if(len(string) == 0):
                return "0"
            else:
                return string

        string += f" - {imaginary}i" if self.imaginary < 0 else f" + {imaginary}i"
        return string

    def conjugate(self):
        return ComplexNumber(self.real, self.imaginary * -1)

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary

        return ComplexNumber(real = real, imaginary = imaginary)

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary

        return ComplexNumber(real = real, imaginary = imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real

        if imaginary == 0:
            return real

        return ComplexNumber(real = real, imaginary = imaginary)

    def __truediv__(self, other):
        result = self.__mul__(other.conjugate())
        denominator = other.__mul__(other.conjugate())

        result.real /= float(denominator)
        result.imaginary /= float(denominator)

        return result
