
class A:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

class B:
    def __init__(self, d: float, e: float):
        self.d = d
        self.e = e

    def sumar_todo(self, aa: float, bb: float) -> float:
        return self.d + self.e + aa + bb

# Asociación
objetoA = A(1.0, 2.0, 3.0)
objetoB = B(4.0, 5.0)
print(objetoB.sumar_todo(objetoA.a, objetoA.b))

class C:
    def __init__(self, d: float, e: float):
        self.d = d
        self.e = e
        self.Aa = A(1.0, 2.0, 3.0)

    def sumar_todo(self) -> float:
        return self.d + self.e + self.Aa.a + self.Aa.b

# Composición
objetoC = C(4.0, 5.0)
print(objetoC.sumar_todo())

class D:
    def __init__(self, d: float, e: float, Aa: A):
        self.d = d
        self.e = e
        self.Aa = Aa

    def sumar_todo(self) -> float:
        return self.d + self.e + self.Aa.a + self.Aa.b

# Agregación
objetoD = D(4.0, 5.0, objetoA)
print(objetoD.sumar_todo())





