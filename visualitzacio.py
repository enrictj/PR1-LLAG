def mostrar_afn(afn):
    """Mostra per pantalla els components d'un AFN."""
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
    """Mostra per pantalla els components d'un AFN-λ."""
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
    """
    Mostra per pantalla els components d'un AFD.
    Si mostrar_mort=False, oculta les transicions a l'estat buit (∅).
    """
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
        if not mostrar_mort and not desti:
            continue
        print(f"  {nom(estat)} --{simbol}--> {nom(desti)}")