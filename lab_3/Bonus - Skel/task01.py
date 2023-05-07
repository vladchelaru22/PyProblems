
class Complex:

    def __init__(self, real_part: int = 0, imaginary_part: int = 0, var_name: str = 'var') -> None:
        self.name=var_name
        self.real=real_part
        self.imag=imaginary_part

    def __str__(self) -> str:
        messege=""
        if self.real == 0 and self.imag!=0:
            messege= f"{self.name} = {self.imag}i"
        if self.imag==0 and self.real!=0:
            messege= f"{self.name} = {self.real}"
        if self.imag==0 and self.real==0:
            messege= f"{self.name} = 0"
        if self.imag<0 and self.real!=0:
            messege= f"{self.name} = {self.real} - {abs(self.imag)}i"
        if (self.real>0 and self.imag>0) or (self.real<0 and self.imag>0):
            messege= f"{self.name} = {self.real} + {self.imag}i"
        return messege

    def add_complex_numbers(self, other) -> None:
        self.real=self.real+other.real
        self.imag=self.imag+other.imag

    def substract_complex_numbers(self, other) -> None:
        self.real = self.real - other.real
        self.imag = self.imag - other.imag

    def multiply_complex_numbers(self, other) -> None:
        # (a + bj) * (c + dj) = (ac - bd) + (ad + bc)j
        new_real=(self.real*other.real)-(self.imag*other.imag)
        new_imag=(self.real*other.imag)+(self.imag*other.real)
        self.real=new_real
        self.imag=new_imag