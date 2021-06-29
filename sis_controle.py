import os
#import pandas as pd
from PySimpleGUI import PySimpleGUI as sg



def cad_fis(cad_fis):
    sg.theme('Reddit')
    layout = [
                  [sg.Text('Nome: ') , sg.Input('')],
                  [sg.Text('Sobrenome: '), sg.Input('')],
                  [sg.Text('Endereço: '),  sg.Input('')],
                  [sg.Text('Número: '), sg.Input('')],
                  [sg.Text('Bairro: '), sg.Input('')],
                  [sg.Text('Cidade: '), sg.Input('')],
                  [sg.Text('Estado: '), sg.Input('')],
                  [sg.Text('Telefone: '), sg.Input('')],
                  [sg.Text('Email: '), sg.Input('')],
                  [sg.Text('CPF: '),  sg.Input('')],
                  [sg.Button('Finalizar cadastro'), sg.Button('Voltar')]
    ]
    #arquivo = open('cadastrofisico.csv', 'a')
    #arquivo.writelines(cad_fis)
    #arquivo.writelines('\n')
    #arquivo.close()

    return sg.Window('Cadastro pessoa física', layout=layout, finalize=True)



def cad_jur(cad_jur):
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome da Empresa: '), sg.Input('')],
        [sg.Text('Endereço: '), sg.Input('')],
        [sg.Text('Número: '), sg.Input('')],
        [sg.Text('Bairro: '), sg.Input('')],
        [sg.Text('Cidade: '), sg.Input('')],
        [sg.Text('Estado: '), sg.Input('')],
        [sg.Text('Telefone: '), sg.Input('')],
        [sg.Text('Email: '), sg.Input('')],
        [sg.Text('CNPJ: '), sg.Input('')],
        [sg.Button('Finalizar cadastro'), sg.Button('Voltar')]

    ]
        #arquivo = open('cadastrojuridico.csv', 'a')
        #arquivo.writelines(cad_jur)
        #arquivo.writelines('\n')
        #arquivo.close()
    return sg.Window('Cadastro jurídico ', layout= layout, finalize= True)


def cad_prod(cad_prod):
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome do produto: '), sg.Input('')],
        [sg.Text('Código: '), sg.Input('')],
        [sg.Text('Quantidade: '), sg.Input('')],
        [sg.Text('Preço:'), sg.Input('')],
        [sg.Button('Finalizar cadastro'), sg.Button('Voltar')]
    ]
        #arquivo = open('cadastroproduto.csv', 'a')
        #arquivo.writelines(cad_prod)
        #arquivo.writelines('\n')
        #arquivo.close()
    return sg.Window('Cadastro de produtos', layout=layout, finalize=True)



def pesqfis(pesqfis):
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome a buscar:'), sg.Input('')],
        [sg.Button('Buscar'), sg.Button('Voltar')]
    ]

    #with open('cadastrofisico.csv', 'r') as arquivo:
     #   for f in arquivo.readlines():
      #      if(f.find(nome) > 1):
       #         print(f)
        #    else:
         #       print('Nome não encontrado.')
    return sg.Window('Busca pessoa física', layout=layout, finalize=True)


def pesqjur(pesqjur):
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome a buscar:'), sg.Input('')],
        [sg.Button('Buscar'), sg.Button('Voltar')]
    ]
   # with open('cadastrojuridico.csv', 'r') as arquivo:
    #    for f in arquivo.readlines():
     #       if (f.find(nome) > 1):
      #          print(f)
       #     else:
        #        print('Nome não encontrado.')
    return sg.Window('Busca pessoa jurídica', layout=layout, finalize=True)



def pesqprod(pesqprod):
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome do produto:'), sg.Input('')],
        [sg.Button('Buscar'), sg.Button('Voltar')]
    ]
    #with open('cadastroproduto.csv', 'r') as arquivo:
     #   for f in arquivo.readlines():
      #      if (f.find(nome) > -1):
       #         print(f)
        #    else:
         #       f.find(nome) == 0
          #      print('Produto não encontrado.')
    return sg.Window('Busca produto', layout=layout, finalize=True)


def tela_inicial():
    layout = [


        [sg.Text('1- Cadastro de pessoa física'), sg.Button('Selecionar 1')],
        [sg.Text('2- Cadastro de pessoa jurídica'), sg.Button('Selecionar 2')],
        [sg.Text('3- Cadastro de produto'), sg.Button('Selecionar 3')],
        [sg.Text('4- Busca pessoa física'), sg.Button('Selecionar 4')],
        [sg.Text('5- Busca pessoa jurídica'), sg.Button('Selecionar 5')],
        [sg.Text('6- Busca produto'), sg.Button('Selecionar 6')],
   ]
    return sg.Window('PyCads alpha', layout=layout, finalize=True)

janela1, janela2, janela3, janela4, janela5, janela6, janela7 = tela_inicial(), None, None, None, None, None, None

while True:
    window,event,values = sg.read_all_windows()


    if window == janela1 and event == sg.WINDOW_CLOSED:
        break

    if window == janela1 and event == 'Selecionar 1':
        janela2 == cad_fis(cad_fis)
        janela1.hide()

    if window == janela2 and event == 'Voltar':
        janela2.hide(cad_fis)
        janela1.un_hide()


    if window == janela1 and event == 'Selecionar 2':
        janela3 == cad_jur(cad_jur)
        janela1.hide()

    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()

    if window == janela1 and event == 'Selecionar 3':
      janela4 == cad_prod(cad_prod)
      janela1.hide()

    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela1.un_hide()

    if window == janela1 and event == 'Selecionar 4':
        janela5 == pesqfis(pesqfis)
        janela1.hide()

    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela1.un_hide()

    if window == janela1 and event == "Selecionar 5":
        janela6 == pesqjur(pesqjur)
        janela1.hide()

    if window == janela6 and event == 'Voltar':
        janela6.hide()
        janela1.un_hide()

    if window == janela1 and event == 'Selecionar 6':
        janela7 ==  pesqprod(pesqprod)
        janela1.hide()

    if window == janela7 and event == 'Voltar':
        janela7.hide()
        janela1.un_hide()

























