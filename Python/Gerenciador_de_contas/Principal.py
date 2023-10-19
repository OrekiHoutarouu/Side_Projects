from modulos import funcoes_do_arquivo, utilidades
import os
from time import sleep

print('='*100)
print('MENU PRINCIPAL'.center(100))
print('='*100)

print('1 - Cadastrar nova conta')
print('2 - Ver contas cadastradas')
print('3 - Deletar alguma conta')
print('4 - Sair do programa')

caminho = os.path.join('./', 'contas')
funcoes_do_arquivo.criarPastaComContas(caminho)

while True:  
    while True:
        try:
            opcao = int(input('Opção: '))
            
            if opcao > 4 or opcao < 1:
                print('Digite uma opção válida.')
                
            else:
                break
            
        except ValueError:
            print('Digite uma opção válida')
                
                
    if opcao == 1:
        print('='*100)
        print('CADASTRAR NOVA CONTA'.center(100))
        print('='*100)
        
        funcoes_do_arquivo.cadastrarContas(
            caminho,
            conta = {
                'plataforma': str(input('Plataforma: ')),
                'email': str(input('E-mail: ')),
                'senha': str(input('Senha: '))
            }
        )
        
        print('='*100)
    
    elif opcao == 2:
        print('='*100)
        print('VER CONTAS CADASTRADAS'.center(100))
        print('='*100)
        
        funcoes_do_arquivo.verContasCadastradas(caminho)
        
        print('-'*100)
    
    elif opcao == 3:
        print('='*100)
        print('EXCLUIR CONTA'.center(100))
        print('='*100)
        
        funcoes_do_arquivo.excluirConta(caminho)
        
    elif opcao == 4:
        print('='*100)
        print('FINALIZANDO PROGRAMA'.center(100))
        print('='*100)
        
        sleep(2)
        
        break