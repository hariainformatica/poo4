class EjemploExcepciones:
    #ZeroDivisionError
    def zeroDivisionError(self, *, num:int, den:int)->int:
        if (den == 0):
            raise ZeroDivisionError
        
        return num // den

    #ValueError

    #FileNotFoundError

    #TypeError

    #PermissionError

    #IndexError

    #KeyboardInterrupt

    #UnicodeDecodeError

    #AttributeError