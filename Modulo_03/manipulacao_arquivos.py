nome_arquivo = 'notas.txt'
print('O que voce quer salvar?')
texto_usuario = input()

arquivo_aberto = open(nome_arquivo, 'w')
arquivo_aberto.write(texto_usuario)
arquivo_aberto.close()

print('Salvo!')

arquivo_aberto = open(nome_arquivo, 'r')
conteudo_final = arquivo_aberto.read()
print('Olha o que eu achei escrito:')
print(conteudo_final)
arquivo_aberto.close()
