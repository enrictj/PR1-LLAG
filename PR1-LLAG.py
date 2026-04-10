from collections import defaultdict, deque

class AFN:
    def __init__(self, estats, alfabet, transicions, inicial, finals):
        self.estats = estats
        self.alfabet = alfabet
        self.transicions = transicions
        self.inicial = inicial
        self.finals = finals


class AFD:
    def __init__(self):
        self.estats = set()
        self.transicions = dict()
        self.inicial = None
        self.finals = set()


def determinitzar(afn):
    afd = AFD()

    estat_inicial = frozenset([afn.inicial])
    afd.inicial = estat_inicial

    cua = deque([estat_inicial])
    visitats = set([estat_inicial])

    while cua:
        estat_actual = cua.popleft()
        afd.estats.add(estat_actual)

        for simbol in afn.alfabet:
            nou_estat = set()

            for subestat in estat_actual:
                if (subestat, simbol) in afn.transicions:
                    nou_estat.update(afn.transicions[(subestat, simbol)])

            nou_estat = frozenset(nou_estat)

            afd.transicions[(estat_actual, simbol)] = nou_estat

            if nou_estat not in visitats:
                visitats.add(nou_estat)
                cua.append(nou_estat)

    for estat in afd.estats:
        if any(subestat in afn.finals for subestat in estat):
            afd.finals.add(estat)

    return afd


def mostrar_afd(afd):
    print("\nESTATS AFD:")
    for e in afd.estats:
        print(set(e))

    print("\nESTAT INICIAL:")
    print(set(afd.inicial))

    print("\nESTATS FINALS:")
    for e in afd.finals:
        print(set(e))

    print("\nTRANSICIONS:")
    for (estat, simbol), desti in afd.transicions.items():
        print(f"{set(estat)} --{simbol}--> {set(desti)}")


# Exemple d’ús

estats = {'q0', 'q1', 'q2'}
alfabet = {'a', 'b'}

transicions = {
    ('q0', 'a'): {'q0', 'q1'},
    ('q0', 'b'): {'q0'},
    ('q1', 'b'): {'q2'}
}

inicial = 'q0'
finals = {'q2'}

afn = AFN(estats, alfabet, transicions, inicial, finals)

afd = determinitzar(afn)

mostrar_afd(afd)