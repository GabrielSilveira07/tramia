from datetime import date

from tramia.models import status as st


class Demanda:
    """Atividade da equipe: reunião, diagnóstico, integração, correção, tarefa interna."""

    def __init__(
        self,
        titulo: str,
        prazo: date,
        responsavel_id: int | None = None,  # None: demanda ainda em análise, sem responsável
        status: str = st.INICIAL,
        id: int | None = None,
    ):
        self.__id = id
        self.titulo = titulo
        self.prazo = prazo
        self.responsavel_id = responsavel_id
        self.status = status

    @property
    def id(self) -> int | None:
        return self.__id

    @id.setter
    def id(self, valor: int) -> None:
        if self.__id is not None:
            raise ValueError("O id já foi definido e não pode ser alterado.")
        self.__id = valor

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        valor = (valor or "").strip()
        if not valor:
            raise ValueError("O título é obrigatório.")
        self.__titulo = valor

    @property
    def prazo(self) -> date:
        return self.__prazo

    @prazo.setter
    def prazo(self, valor: date) -> None:
        # O model trabalha com date; converter texto (dd/mm/aaaa ou ISO) é papel
        # da interface e do DAO, não do domínio.
        if not isinstance(valor, date):
            raise TypeError("O prazo deve ser uma data (datetime.date).")
        self.__prazo = valor

    @property
    def responsavel_id(self) -> int | None:
        return self.__responsavel_id

    @responsavel_id.setter
    def responsavel_id(self, valor: int | None) -> None:
        self.__responsavel_id = valor

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, valor: str) -> None:
        self.__status = st.validar(valor)

    # Regras de domínio: ficam no model, não no menu, para o front futuro reutilizar.

    @property
    def tem_responsavel(self) -> bool:
        return self.__responsavel_id is not None

    @property
    def atrasada(self) -> bool:
        return self.__prazo < date.today() and self.__status not in st.FINAIS

    def __repr__(self) -> str:
        return f"Demanda(id={self.__id}, titulo={self.__titulo!r}, status={self.__status!r})"
