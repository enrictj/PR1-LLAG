class AFN:
    """Autòmat Finit No determinista."""

    def __init__(self, estats, alfabet, transicions, inicial, finals):
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


    def __repr__(self):
        return (f"AFD(estats={self.estats}, "
                f"inicial={self.inicial}, finals={self.finals})")