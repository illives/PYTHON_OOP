from classes import Cliente

cliente1 = Cliente('Zezinho', 31)
cliente1.insere_endereco('São Paulo', 'MG')

print(cliente1.nome)
cliente1.lista_enderecos()

del cliente1#Uma vez excluido o Cliente1, os dados da classe endereço tambem será apagada.