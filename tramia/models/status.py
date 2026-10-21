# =============================================================================
# STATUS — PROVISÓRIO
#
# A forma de armazenar o status (texto livre, lista com CHECK ou tabela própria)
# e o valor padrão são decisões de modelagem do Gabriel (pilar BD).
# Este módulo é o ÚNICO ponto que conhece os status: models, DAOs e interfaces
# importam daqui. Quando a decisão sair, só este arquivo (e o schema) muda.
# =============================================================================

ABERTA = "aberta"
EM_ANDAMENTO = "em_andamento"
CONCLUIDA = "concluida"

VALIDOS = (ABERTA, EM_ANDAMENTO, CONCLUIDA)
FINAIS = (CONCLUIDA,)  # status em que a demanda não conta como atrasada
INICIAL = ABERTA


def validar(status: str) -> str:
    if status not in VALIDOS:
        raise ValueError(f"Status inválido: {status!r}. Válidos: {', '.join(VALIDOS)}")
    return status
