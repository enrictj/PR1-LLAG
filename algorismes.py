from collections import deque
from models import AFD


def lambda_clausura(estats, transicions_lambda):
    """
    Calcula el conjunt d'estats assolibles des d'un conjunt d'estats
    seguint només transicions lambda (sense consumir cap símbol).
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
    Converteix un AFN a un AFD equivalent
    mitjançant la construcció de subconjunts.
    """
    afd = AFD(alfabet=afn.alfabet)

    estat_inicial = frozenset([afn.inicial])
    afd.inicial = estat_inicial

    cua = deque([estat_inicial])
    visitats = {estat_inicial}

    while cua:
        estat_actual = cua.popleft()
        afd.estats.add(estat_actual)

        for simbol in afn.alfabet:
            nou_estat = frozenset(
                s for subestat in estat_actual
                if (subestat, simbol) in afn.transicions
                for s in afn.transicions[(subestat, simbol)]
            )
            afd.transicions[(estat_actual, simbol)] = nou_estat
            if nou_estat not in visitats:
                visitats.add(nou_estat)
                cua.append(nou_estat)

    for estat in afd.estats:
        if any(subestat in afn.finals for subestat in estat):
            afd.finals.add(estat)

    return afd


def determinitzar_afnl(afnl):
    """
    Converteix un AFN-λ a un AFD equivalent aplicant
    la lambda-clausura a cada pas de la construcció de subconjunts.
    """
    afd = AFD(alfabet=afnl.alfabet)

    estat_inicial = lambda_clausura([afnl.inicial], afnl.transicions_lambda)
    afd.inicial = estat_inicial

    cua = deque([estat_inicial])
    visitats = {estat_inicial}

    while cua:
        estat_actual = cua.popleft()
        afd.estats.add(estat_actual)

        for simbol in afnl.alfabet:
            estats_desti = set(
                s for subestat in estat_actual
                if (subestat, simbol) in afnl.transicions
                for s in afnl.transicions[(subestat, simbol)]
            )
            nou_estat = lambda_clausura(estats_desti, afnl.transicions_lambda)
            afd.transicions[(estat_actual, simbol)] = nou_estat
            if nou_estat not in visitats:
                visitats.add(nou_estat)
                cua.append(nou_estat)

    for estat in afd.estats:
        if any(subestat in afnl.finals for subestat in estat):
            afd.finals.add(estat)

    return afd