from collections import deque
class AFN:
    def __init__(self, estats, alfabet, transicions, inicial, finals):
        self.estats = estats          # conjunt d'estats
        self.alfabet = alfabet        # conjunt de símbols
        self.transicions = transicions  # dict: (estat, simbol) -> set d'estats
        self.inicial = inicial        # estat inicial
        self.finals = finals          # conjunt d'estats finals
        
class AFNL:
    def __init__(self, estats, alfabet, transicions, transicions_lambda, inicial, finals):
        self.estats = estats
        self.alfabet = alfabet
        self.transicions = transicions           
        self.transicions_lambda = transicions_lambda  # dict: estat -> set d'estats (transicions buides)
        self.inicial = inicial
        self.finals = finals

class AFD:
    def __init__(self):
        self.estats = set()       # cada estat és un frozenset d'estats de l'AFN
        self.transicions = dict() # dict: (frozenset, simbol) -> frozenset
        self.inicial = None
        self.finals = set()

def lambda_clausura(estats, transicions_lambda):
    """
    Calcula la λ-clausura d'un conjunt d'estats:
    retorna tots els estats accessibles únicament amb λ-transicions.
    """
    clausura = set(estats)
    cua = deque(estats)
    while cua:
        estat = cua.popleft()
        for desti in transicions_lambda.get(estat, set()):
            if desti not in clausura:
                clausura.add(desti)
                cua.append(desti)
    return frozenset(clausura)

def determinitzar_afn(afn):
    """
    Converteix un AFN en un AFD equivalent mitjançant la construcció de subconjunts.
    Cada estat de l'AFD és un subconjunt (frozenset) d'estats de l'AFN.
    """
    afd = AFD()

    # L'estat inicial de l'AFD és el conjunt format per l'estat inicial de l'AFN
    estat_inicial = frozenset([afn.inicial])
    afd.inicial = estat_inicial

    cua = deque([estat_inicial])
    visitats = set([estat_inicial])

    while cua:
        estat_actual = cua.popleft()
        afd.estats.add(estat_actual)

        for simbol in afn.alfabet:
            # Unim tots els estats destí de cada subestat amb el símbol actual
            nou_estat = frozenset(
                s for subestat in estat_actual
                  if (subestat, simbol) in afn.transicions
                  for s in afn.transicions[(subestat, simbol)]
            )
            afd.transicions[(estat_actual, simbol)] = nou_estat

            # Si el nou estat no ha estat visitat, l'afegim a la cua
            if nou_estat not in visitats:
                visitats.add(nou_estat)
                cua.append(nou_estat)

    # Un estat de l'AFD és final si conté algun estat final de l'AFN
    for estat in afd.estats:
        if any(subestat in afn.finals for subestat in estat):
            afd.finals.add(estat)

    return afd

def determinitzar_afnl(afnl):
    """
    Converteix un AFN-λ en un AFD equivalent.
    A diferència de determinitzar_afn, aplica la λ-clausura a cada pas.
    """
    afd = AFD()

    # L'estat inicial és la λ-clausura de l'estat inicial de l'AFN-λ
    estat_inicial = lambda_clausura([afnl.inicial], afnl.transicions_lambda)
    afd.inicial = estat_inicial

    cua = deque([estat_inicial])
    visitats = set([estat_inicial])

    while cua:
        estat_actual = cua.popleft()
        afd.estats.add(estat_actual)

        for simbol in afnl.alfabet:
            # Calculem els estats destí directes amb el símbol
            estats_desti = set(
                s for subestat in estat_actual
                  if (subestat, simbol) in afnl.transicions
                  for s in afnl.transicions[(subestat, simbol)]
            )
            # Apliquem la λ-clausura als estats destí
            nou_estat = lambda_clausura(estats_desti, afnl.transicions_lambda)
            afd.transicions[(estat_actual, simbol)] = nou_estat

            if nou_estat not in visitats:
                visitats.add(nou_estat)
                cua.append(nou_estat)

    # Un estat de l'AFD és final si conté algun estat final de l'AFN-λ
    for estat in afd.estats:
        if any(subestat in afnl.finals for subestat in estat):
            afd.finals.add(estat)

    return afd

def mostrar_afn(afn):
    print("ESTATS:")
    print(" ", afn.estats)
    print("\nESTAT INICIAL:")
    print(" ", afn.inicial)
    print("\nESTATS FINALS:")
    print(" ", afn.finals)
    print("\nTRANSICIONS:")
    for (estat, simbol), desti in afn.transicions.items():
        print(f"  {estat} --{simbol}--> {desti}")

def mostrar_afnl(afnl):
    print("ESTATS:")
    print(" ", afnl.estats)
    print("\nESTAT INICIAL:")
    print(" ", afnl.inicial)
    print("\nESTATS FINALS:")
    print(" ", afnl.finals)
    print("\nTRANSICIONS:")
    for (estat, simbol), desti in afnl.transicions.items():
        print(f"  {estat} --{simbol}--> {desti}")
    print("\nTRANSICIONS LAMBDA:")
    for estat, desti in afnl.transicions_lambda.items():
        print(f"  {estat} --λ--> {desti}")

def mostrar_afd(afd, mostrar_mort=True):
    # Representa un frozenset buit com a estat mort ∅
    def nom(e):
        return '∅' if not e else str(set(e))

    print("ESTATS:")
    for e in afd.estats:
        print(" ", nom(e))
    print("\nESTAT INICIAL:")
    print(" ", nom(afd.inicial))
    print("\nESTATS FINALS:")
    for e in afd.finals:
        print(" ", nom(e))
    print("\nTRANSICIONS:")
    for (estat, simbol), desti in afd.transicions.items():
        print(f"  {nom(estat)} --{simbol}--> {nom(desti)}")

# Exemple 1: AFN sense lambda-transicions
afn = AFN(
    estats={'q0', 'q1', 'q2'},
    alfabet={'a', 'b'},
    transicions={
        ('q0', 'a'): {'q0', 'q1'}, 
        ('q0', 'b'): {'q0'},
        ('q1', 'b'): {'q2'},
    },
    inicial='q0',
    finals={'q2'}
)

print("\n" + "=" * 40)
print("EXEMPLE 1 - AFN ORIGINAL")
print("=" * 40)
mostrar_afn(afn)

print("\n" + "=" * 40)
print("EXEMPLE 1 - AFD DETERMINITZAT")
print("=" * 40)
afd1 = determinitzar_afn(afn)
mostrar_afd(afd1)

# Exemple 2: AFN amb lambda-transicions
afnl = AFNL(
    estats={0, 1, 2, 3, 4, 5, 6},
    alfabet={'0', '1'},
    transicions={
        (1, '0'): {1},   
        (1, '1'): {2},
        (2, '1'): {3},
        (3, '0'): {4},
        (4, '0'): {6},
        (5, '1'): {3},
        (6, '0'): {6},   
        (6, '1'): {6},
    },
    transicions_lambda={
        0: {1},  # λ-clausura(0) = {0, 1}
        4: {5},  # λ-clausura(4) = {4, 5}
    },
    inicial=0,
    finals={6}
)

print("\n" + "=" * 40)
print("EXEMPLE 2 - AFN-λ ORIGINAL")
print("=" * 40)
mostrar_afnl(afnl)

print("\n" + "=" * 40)
print("EXEMPLE 2 - AFN-λ DETERMINITZAT")
print("=" * 40)
afd2 = determinitzar_afnl(afnl)
mostrar_afd(afd2)