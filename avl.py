class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.altura = 1
        self.izquierda = None
        self.derecha = None

class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if nodo is None:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def insertar(self, raiz, valor):
        if raiz is None:
            return NodoAVL(valor)
        elif valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor)

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))

        balance = self.balance(raiz)

        # Rotaciones para balancear el árbol
        if balance > 1 and valor < raiz.izquierda.valor:
            return self.rotacion_derecha(raiz)
        if balance < -1 and valor > raiz.derecha.valor:
            return self.rotacion_izquierda(raiz)
        if balance > 1 and valor > raiz.izquierda.valor:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)
        if balance < -1 and valor < raiz.derecha.valor:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y

    def rotacion_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y

    def eliminar(self, raiz, valor):
        if raiz is None:
            return raiz

        if valor < raiz.valor:
            raiz.izquierda = self.eliminar(raiz.izquierda, valor)
        elif valor > raiz.valor:
            raiz.derecha = self.eliminar(raiz.derecha, valor)
        else:
            if raiz.izquierda is None:
                temp = raiz.derecha
                raiz = None
                return temp
            elif raiz.derecha is None:
                temp = raiz.izquierda
                raiz = None
                return temp

            temp = self.min_valor_nodo(raiz.derecha)
            raiz.valor = temp.valor
            raiz.derecha = self.eliminar(raiz.derecha, temp.valor)

        if raiz is None:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))

        balance = self.balance(raiz)

        if balance > 1 and self.balance(raiz.izquierda) >= 0:
            return self.rotacion_derecha(raiz)

        if balance < -1 and self.balance(raiz.derecha) <= 0:
            return self.rotacion_izquierda(raiz)

        if balance > 1 and self.balance(raiz.izquierda) < 0:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)

        if balance < -1 and self.balance(raiz.derecha) > 0:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual
