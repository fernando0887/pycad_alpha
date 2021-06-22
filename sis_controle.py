import os
import pandas as pd



def cad_fis(cad_fis):
        cad_fis = {'Nome: ' + input('Nome: ') + ' ' + 'Sobrenome: ' + input('Sobrenome: ') + ', ' +
                   'Endereço: ' + input('Endereço: ') +  ', ' + 'Número: ' + input('Número: ') + ', ' +'Bairro: ' + input('Bairro: ') + ','
                   + 'Cidade: ' + input('Cidade: ') + ', ' + 'Estado: ' + input('Estado: ') + ', ' + 'Telefone: ' + input('Telefone: ')
                   + ', ' + 'Email: ' + input('Email: ') + ', ' + 'CPF: ' + input('CPF: ') }
        arquivo = open('cadastrofisico.csv', 'a')
        arquivo.writelines(cad_fis)
        arquivo.writelines('\n')
        arquivo.close()
        return print('Dados cadastrados: ', cad_fis)



def cad_jur(cad_jur):
        cad_jur = {'Nome: ' + input('Nome: ') + ' ' + 'Sobrenome: ' + input('Sobrenome: ') + ', ' +
                   'Endereço: ' + input('Endereço: ') +  ', ' + 'Número: ' + input('Número: ') + ', ' +'Bairro: ' + input('Bairro: ') + ','
                   + 'Cidade: ' + input('Cidade: ') + ', ' + 'Estado: ' + input('Estado: ') + ', ' + 'Telefone: ' + input('Telefone: ')
                   + ', ' + 'Email: ' + input('Email: ') + ', ' + 'CNPJ':  + input('CNPJ: ') }
        arquivo = open('cadastrojuridico.csv', 'a')
        arquivo.writelines(cad_jur)
        arquivo.writelines('\n')
        arquivo.close()
        return print('Dados da empresa cadastrada: ', cad_jur)



def cad_prod(cad_prod):
        cad_prod = {'Nome: ' + input('Nome: ') + ' ' + 'Código: ' + input('Código do produto: ') + ', ' +
                   'Quantidade: ' + input('Quantidade: ') +  ', ' + 'Preço: ' + input('Preço: R$  ') }
        arquivo = open('cadastroproduto.csv', 'a')
        arquivo.writelines(cad_prod)
        arquivo.writelines('\n')
        arquivo.close()
        return print('Produto: ', cad_prod)



def pesqfis(pesqfis):
    nome = input('Insira o nome:')
    with open('cadastrofisico.csv', 'r') as arquivo:
        for f in arquivo.readlines():
            if(f.find(nome) > -1):
                print(f)
            else:
                print('Nome não encontrado.')



def pesqjur(pesqjur):
    nome = input('Insira o nome:')
    with open('cadastrojuridico.csv', 'r') as arquivo:
        for f in arquivo.readlines():
            if (f.find(nome) > 1):
                print(f)
            else:
                print('Nome não encontrado.')



def pesqprod(pesqprod):
    nome = input('Insira o nome:')
    with open('cadastroproduto.csv', 'r') as arquivo:
        for f in arquivo.readlines():
            if (f.find(nome) > -1):
                print(f)
            else:
                print('Produto não encontrado.')





while True:


        print(' ***** PyCads alpha *****\n\n '
              
                        'Selecione a opção desejada:\n'
                        '1- Cadastro de pessoa física\n'
                        '2- Cadastro de pessoa jurídica\n'
                        '3- Cadastro de produto\n'
                        '4- Busca pessoa física\n'
                        '5- Busca pessoa jurídica\n'
                        '6- Busca produto\n'
                        '0- Sair\n')



        menu = input('Opção:')
        if menu == '1':

                cad_fis(cad_fis)
                s = input('Voltar ao menu principal? (digite S ou N para sair):')
                if s == 'S' or 's':
                        continue
                else:
                        s == 'N' or 'n'
                        break



        elif menu == '2':
                cad_jur(cad_jur)
                s = input('Voltar ao menu principal? (digite S ou N para sair):')
                if s == 'S' or 's':
                       continue
                else:
                       break



        elif menu == '3':
                cad_prod(cad_prod)
                s = input('Voltar ao menu principal? (digite S ou N para sair):')
                if s == 'S' or 's':
                      continue
                else:
                       break



        elif menu == '4':
                pesqfis(pesqfis)
                break



        elif menu == '5':
                pesqjur(pesqjur)
                break



        elif menu == '6':
                pesqprod(pesqprod)
                break



        elif menu == '0':
                print('*****Saindo*****')
                break
























