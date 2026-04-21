from models import AFN, AFNL
from algorismes import determinitzar_afn, determinitzar_afnl
from visualitzacio import mostrar_afn, mostrar_afnl, mostrar_afd


def exemple1():
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

    print("=" * 40)
    print("EXEMPLE 1 - AFN ORIGINAL")
    print("=" * 40)
    mostrar_afn(afn)

    print("\n" + "=" * 40)
    print("EXEMPLE 1 - AFD DETERMINITZAT")
    print("=" * 40)
    afd = determinitzar_afn(afn)
    mostrar_afd(afd)

    print("\nPROVES:")
    for paraula in ["ab", "aab", "abb", "b", "ba"]:
        resultat = "ACCEPTA" if afd.accepta(paraula) else "REBUTJA"
        print(f"  '{paraula}' -> {resultat}")


def exemple2():
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
            0: {1},
            4: {5},
        },
        inicial=0,
        finals={6}
    )

    print("\n" + "=" * 40)
    print("EXEMPLE 2 - AFN-λ ORIGINAL")
    print("=" * 40)
    mostrar_afnl(afnl)

    print("\n" + "=" * 40)
    print("EXEMPLE 2 - AFD DETERMINITZAT")
    print("=" * 40)
    afd = determinitzar_afnl(afnl)
    mostrar_afd(afd)


if __name__ == "__main__":
    exemple1()
    exemple2()