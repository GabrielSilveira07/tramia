from datetime import date

from tramia.database.criar_banco import criar_banco
from tramia.database.conexao import conectar
from tramia.dao.demandaDAO import DemandaDAO
from tramia.models.demanda import Demanda

criar_banco()
dao = DemandaDAO()

d = Demanda("Teste inserir", date(2026, 11, 20))
dao.inserir(d)

print("id do objeto:", d.id)
c = conectar()
print("linha no banco:", dict(c.execute("SELECT * FROM demanda WHERE id = ?", (d.id,)).fetchone()))
c.close()