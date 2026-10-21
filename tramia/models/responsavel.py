class Responsavel:
    """Pessoa da equipe que assume demandas."""

    def __init__(self, nome: str, email: str, id: int | None = None):
        self.__id = id
        self.nome = nome    # passa pelo setter (validação)
        self.email = email  # passa pelo setter (validação)

    # Encapsulamento: atributos privados (__) expostos por property.
    # A validação fica no setter, então nenhum objeto existe em estado inválido.

    @property
    def id(self) -> int | None:
        return self.__id

    @id.setter
    def id(self, valor: int) -> None:
        if self.__id is not None:
            raise ValueError("O id já foi definido e não pode ser alterado.")
        self.__id = valor

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None:
        valor = (valor or "").strip()
        if not valor:
            raise ValueError("O nome é obrigatório.")
        self.__nome = valor

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, valor: str) -> None:
        valor = (valor or "").strip()
        if "@" not in valor:
            raise ValueError("E-mail inválido.")
        self.__email = valor

    def __repr__(self) -> str:
        return f"Responsavel(id={self.__id}, nome={self.__nome!r})"
