class AFN:
    """Autòmat Finit No determinista."""

    def __init__(self, estats, alfabet, transicions, inicial, finals):
        assert inicial in estats, f"L'estat inicial '{inicial}' no és a estats"
        assert set(finals) <= set(estats), "Hi ha estats finals fora de estats"

        self.estats = estats
        self.alfabet = alfabet
        self.transicions = transicions
        self.inicial = inicial
        self.finals = finals

    def __repr__(self):
        return (f"AFN(estats={self.estats}, alfabet={self.alfabet}, "
                f"inicial={self.inicial}, finals={self.finals})")


class AFNL:
    """Autòmat Finit No determinista amb transicions Lambda (epsilon)."""

    def __init__(self, estats, alfabet, transicions, transicions_lambda, inicial, finals):
        assert inicial in estats, f"L'estat inicial '{inicial}' no és a estats"
        assert set(finals) <= set(estats), "Hi ha estats finals fora de estats"

        self.estats = estats
        self.alfabet = alfabet
        self.transicions = transicions
        self.transicions_lambda = transicions_lambda
        self.inicial = inicial
        self.finals = finals

    def __repr__(self):
        return (f"AFNL(estats={self.estats}, alfabet={self.alfabet}, "
                f"inicial={self.inicial}, finals={self.finals})")


class AFD:
    """Autòmat Finit Determinista."""

    def __init__(self, estats=None, alfabet=None, transicions=None, inicial=None, finals=None):
        self.estats = estats if estats is not None else set()
        self.alfabet = alfabet if alfabet is not None else set()
        self.transicions = transicions if transicions is not None else dict()
        self.inicial = inicial
        self.finals = finals if finals is not None else set()

    def accepta(self, paraula):
        """Retorna True si l'AFD accepta la paraula donada."""
        estat = self.inicial
        for simbol in paraula:
            estat = self.transicions.get((estat, simbol), frozenset())
        return estat in self.finals

    def __repr__(self):
        return (f"AFD(estats={self.estats}, "
                f"inicial={self.inicial}, finals={self.finals})")