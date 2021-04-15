from .classe_conta import Cliente
from .classe_conta import Conta

Makson = Cliente("Makson Vinicio", 88853674)
conta1 = Conta([Makson], 1, 3000)
conta1.resumo()
