# Validador/gerador de CPF

#cpf de teste: 593.726.730-30
#cpf de teste: 59372673030
import os
import random
import sys
contador = 10

while True:
    os.system('cls')
    menu_escolha = input('Escolha uma opção: \n1 - Gerar CPF\n2 - Validar CPF\n3 - Sair\n')

    if menu_escolha == '3':
        sys.exit()

    if menu_escolha == '2':
        while True:
            contador = 10
            os.system('cls')
            input_cpf_bruto = input('Digite o CPF sem pontuação: ') \
                .replace('.', '') \
                .replace('-', '') \
                .replace(' ', '')
            if not input_cpf_bruto.isnumeric():
                print('Digite apenas números')
                input('Aperte enter para continuar')
                continue
            if len(input_cpf_bruto) >= 12 or len(input_cpf_bruto) <= 10:
                print('Digite apenas 11 números')
                input('Aperte enter para continuar')
                continue
            entrada_repetida = input_cpf_bruto == input_cpf_bruto[0] * len(input_cpf_bruto)
            if entrada_repetida: 
                print('Não é permitido números repetidos')
                input('Aperte enter para continuar')
                continue


            primeiros_nove_digitos = input_cpf_bruto[:9]
            print(primeiros_nove_digitos)

            resultado = 0
            for digito in primeiros_nove_digitos:
                resultado += int(digito) * contador
                print(f'{digito} * {contador} = {int(digito) * contador}')
                contador -= 1
            digito = (resultado * 10) % 11
            print(f'({resultado} * 10) % 11 = {digito}')
            digito = 0 if digito >= 9 else digito
            
            #segundo digito final do cpf

            primeiros_dez_digitos = primeiros_nove_digitos + str(digito)
            contador = 11
            resultado = 0 
            for digito_dois in primeiros_dez_digitos:
                resultado += int(digito_dois) * contador
                print(f'{digito_dois} * {contador} = {int(digito_dois) * contador}')
                contador -= 1
            digito_dois = (resultado * 10) % 11
            print(f'({resultado} * 10) % 11 = {digito_dois}')
            digito_dois = 0 if digito_dois >= 9 else digito_dois

            print(f'CPF: {primeiros_dez_digitos}{digito_dois} é', 'valido' if input_cpf_bruto == primeiros_dez_digitos + str(digito_dois) else 'inválido')
            input('Aperte enter para continuar')
            break

    if menu_escolha == '1':
        while True:
            contador = 10
            os.system('cls')
            nove_digitos = ''
            for _ in range(9):
                nove_digitos += str(random.randint(0, 9))

            primeiros_nove_digitos = nove_digitos
            print(primeiros_nove_digitos)

            resultado = 0
            for digito in primeiros_nove_digitos:
                resultado += int(digito) * contador
                print(f'{digito} * {contador} = {int(digito) * contador}')
                contador -= 1
            digito = (resultado * 10) % 11
            print(f'({resultado} * 10) % 11 = {digito}')
            digito = 0 if digito >= 9 else digito
            
            #segundo digito final do cpf

            primeiros_dez_digitos = primeiros_nove_digitos + str(digito)
            contador = 11
            resultado = 0 
            for digito_dois in primeiros_dez_digitos:
                resultado += int(digito_dois) * contador
                print(f'{digito_dois} * {contador} = {int(digito_dois) * contador}')
                contador -= 1
            digito_dois = (resultado * 10) % 11
            print(f'({resultado} * 10) % 11 = {digito_dois}')
            digito_dois = 0 if digito_dois >= 9 else digito_dois
            novo_cpf = primeiros_dez_digitos + str(digito_dois)
            print(f'CPF: {novo_cpf}')
            input('Aperte enter para continuar')
            break    
