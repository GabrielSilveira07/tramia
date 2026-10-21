# Tramia: sistema interno de demandas

Sistema interno da Tramia para gestão das demandas da equipe: o que está aberto, com quem está e o que está atrasado. Uso interno, não é vendido.

Projeto da disciplina de **Programação Orientada a Objetos** (ADS, Senac Ponta Grossa). É o primeiro recorte do sistema modelado em Banco de Dados I.

## Requisitos

- Python 3.10 ou superior
- Sem dependências externas (`sqlite3` é da biblioteca padrão)

## Como rodar

```bash
python main.py
```

O banco é criado automaticamente em `dados/tramia.db`.

## Estrutura

```
tramia/
  config.py            caminho absoluto do banco
  database/            conexão e criação do schema
  models/              classes de domínio (Responsavel, Demanda) e status
  dao/                 acesso a dados, uma classe por entidade
  interface/terminal/  menu de terminal
main.py                ponto de entrada
```

Cada camada tem uma responsabilidade:

- **models:** regras e validações do domínio, sem saber que existe banco.
- **dao:** SQL e conversão entre linhas do banco e objetos.
- **interface:** entrada e saída, sem regra de negócio.

Assim, uma interface web futura pode reutilizar models e DAOs sem alteração.

## Estado

- [x] Estrutura, configuração e conexão
- [x] Models `Responsavel` e `Demanda` com encapsulamento
- [ ] DAOs
- [ ] Menu de terminal: cadastrar demanda; listar por responsável ou status
- [ ] Extra: atualizar status e excluir

> **Provisório:** o schema em `database/criar_banco.py` e os status em `models/status.py` são temporários. Eles serão substituídos pela modelagem definitiva do sistema, feita na disciplina de Banco de Dados I.
