#PROJETO FOI DESENVOLVIDO POR:
# RAMON 
# IZABELLA
# JÃO PEDRO
#ALUNOS DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS (TADS)
#INSTITUIÇÃO DE ENSINO SUPERIOR: FAESA - CENTRO UNIVERSITÁRIO (CAMPUS: VITÓRIA-ES)

#COMANDO PARA LIMPAR O TERMINAL:
import os
clear = lambda: os.system('cls')
clear()

#INICIO DO PROGRAMA
#ABAIXO ESTÁ UM PEQUENO BANCO DE DADOS QUE VAI ARMAZENAR E VALIDAR ENTRADA DOS USUÁRIOS:
usuarios = ["god","adm","samuel","tuca","gal"]
senhas=    ["0"  ,  "1",     "2",   "3",  "4"]

#ESTES SÃO CONTADORES USADOS NO LAÇOS DE REPETIÇÃO FOR (ARMAZENA A POSIÇÃO DAS LISTAS)
contador = 0
contador2 = 0
a=0

#SÃO VARIAVÉS USADAS NOS LAÇOS DE REPETIÇÃO WHILE(COM O VALOR TRUE INICIAL O LAÇO FICA INFINITO,
# DANDO AO CÓDIGO MAIS FLUIDES E VOLTANDO PARA LINHA OU OPÇÕES PASSADAS)
programa = True
entrarPrograma = False
pergunta = True

while programa:
    while entrarPrograma == False:
        clear()
        pergunta = True
        print("FAÇA O LOGIN PARA ENTRAR NO SISTEMA: ")
        usuarioDigitado = input("DIGITE SEU USUÁRIO: ").lower()
        for x in usuarios:
            contador += 1
            if x in usuarioDigitado:
                a = contador - 1
                senhaDigitado = input("DIGITE A SENHA DO SEU USUÁRIO: ").lower()
                if senhaDigitado == senhas[a]:
                    contador = 0
                    entrarPrograma = True
                    break
                if senhaDigitado != senhas[a]:
                    clear()
                    contador = 0
                    print("     SENHA INVÁLIDA!")
                    break
                else:
                    entrarPrograma = False
            elif contador == len(usuarios):
                clear()
                print("\n     USUÁRIO INVÁLIDO!")
                while pergunta:
                    print("\n DESEJA CADASTRA UM NOVO USUÁRIO? ")
                    print("\nMENU OPÇÕES DE ESCOLHA:")
                    print("    1 - SIM\n    2 - NÃO")
                    respostaPergunta = input("DIGITE O NÚMERO DA OPÇÃO DESEJADA: ").lower()
                    clear()
                    if respostaPergunta == "1" or respostaPergunta == "sim":
                        while pergunta:
                            print("\nDIGITE UM NOME DE USUÁRIO VÁLIDO, PARA CADASTRO:")
                            novoUsuario = input("NOVO USUÁRIO: ").lower()
                            for x in usuarios:
                                contador2 += 1
                                if x in novoUsuario:
                                    clear()
                                    print("\n     USUÁRIO JÁ EXISTE. DIGITE OUTRO NOME!")
                                    contador2 = 0
                                    break
                                elif contador2 == len(usuarios): 
                                    usuarios.append(novoUsuario)
                                    senhaNovoUsuario = input("NOVA SENHA: ").lower()
                                    repetiSenhaNovoUsuario = input("REPITA A SENHA: ").lower()
                                    if senhaNovoUsuario == repetiSenhaNovoUsuario:
                                        senhas.append(senhaNovoUsuario)
                                        contador = 0
                                        pergunta = False
                                        break
                                    else:
                                        clear()
                                        del usuarios[contador2]
                                        contador2 = 0
                                        print("     ERRO: AS SENHAS NÃO SÃO IGUAIS!")
                                        break
                    elif respostaPergunta == "2" or respostaPergunta == "não" or respostaPergunta == "nao":
                        contador = 0
                        entrarPrograma = False
                        break
                    else:
                        clear()
                        print("     OPÇÃO INVÁLIDA. DIGITE SIM OU NÃO!")
                break
        break
    if entrarPrograma == True:
        programa = False
        break

#DENTRO DO PROGRAMA:
programa = True
contador = 0
contador2 = 0

opcaoCadastro1 = True
opcaoCadastro2 = True

opcaoExclusao1 = True
opcaoExclusao2 = True

opcaoModificacao1 = True
opcaoModificacao2 = True

opcaoVerificacao1 = True
opcaoVerificacao2 = True

listaProfessores = ["ramon","izabella","joão"]
listaDisciplinas = ["matemática","química","física"]

clear()
while programa:
    print("Olá ",x,", Seja bem-vindo(a)!\nAqui você consegue controlar a lista de matrículas de professores da escola.")
    print("Os comandos que você pode realizar são:")
    print("     1 - Incluir novo registro;\n     2 - Excluir um registro;\n     3 - Modificar um registro existente;\n     4 - Verificar registro existente;\n     0 - Sair")
    comando = input("Qual tarefa deseja realizar hoje?\nDigite o número da tarefa: ").lower()
    clear()
    if comando == "1":
        #bloco de código de inclusão
        opcaoCadastro1 = True 
        while opcaoCadastro1:
            print("- SISTEMA DE CADASTRO:")
            nomeProfessor = input("Digite o nome do professor que deseja cadastrar: ").lower()
            listaProfessores.append(nomeProfessor)
            nomeDiciplina = input("Digite qual disciplina esse professor leciona: ").lower()
            listaDisciplinas.append(nomeDiciplina)
            clear()
            print("     Professor(a) cadastrado com sucesso!")
            opcaoCadastro2 = True 
            while opcaoCadastro2:
                print("Deseja cadastra outro professor? ")
                print("Menu opções de escolha:")
                print("    1 - Sim\n    2 - Não")
                escolha = input("Digite o número da opção: ").lower()
                if escolha == "1" or escolha == "sim":
                    opcaoCadastro2 = False
                    clear()
                    continue
                elif escolha == "2" or escolha == "não" or escolha == "nao":
                    opcaoCadastro1 = False
                    opcaoCadastro2 = False 
                    clear()
                    break
                else:
                    clear()
                    print("     Opção inválida!")
                    continue
    elif comando == "2":
        #bloco de código de exclusão
        print("- SISTEMA DE EXCLUSÃO DE CADASTRO:")
        opcaoExclusao1 = True
        opcaoExclusao2 = True
        while opcaoExclusao1:
            while opcaoExclusao2:
                contador = 0
                print("Os registros existentes até o momento são:")
                for p in listaProfessores:
                        print("     ",contador," - Professor:", p,"\n           Disciplina:", listaDisciplinas[contador],"\n")
                        contador += 1
                        if contador == len(listaProfessores):
                            break
                print("Deseja excluir um professor?\n   1 - Sim\n   2 - Não\n   0 - Sair")
                excluir = input("Digite o número da opção: ").lower()
                if excluir == "1" or excluir == "sim":
                    numeroProfessor2 = int(input("Infome o número do professor que deseja excluir: "))
                    for lp in range(len(listaProfessores)):
                        if lp == numeroProfessor2:
                            del listaProfessores[lp]
                            del listaDisciplinas[lp]
                            clear()
                            print("     Professor(a) excluido com sucesso!")
                            break
                        elif numeroProfessor2 > len(listaProfessores):
                            clear()
                            print("     Professor não encontado ou a opção está inválida!")
                            break
                elif excluir == "2" or excluir == "não" or excluir == "nao":
                    clear()
                    contador = 0
                    print("Os registros existentes até o momento são:")
                    for p in listaProfessores:
                        print("     ",contador," - Professor:", p,"\n           Disciplina:", listaDisciplinas[contador],"\n")
                        contador += 1
                        if contador == len(listaProfessores):
                            break
                    opcaoExclusao1 = False
                    opcaoExclusao2 = False
                    break
                elif excluir == "0" or excluir == "sair":
                    opcaoExclusao1 = False
                    opcaoExclusao2 = False
                    clear()
                    break
                else:
                    clear()
                    print("     Opção inválida!")
                    break
    elif comando == "3":
        # bloco de código de modificação
        print("- SISTEMA DE MODIFICAÇÃO:")
        opcaoModificacao1 = True
        opcaoModificacao2 = True
        while opcaoModificacao1:
            contador = 0
            print("Os registros existentes até o momento são:")
            for p in listaProfessores:
                print("     ",contador," - Professor:", p,"\n           Disciplina:", listaDisciplinas[contador],"\n")
                contador += 1
                if contador == len(listaProfessores):
                    break
            while opcaoModificacao2:
                print("Deseja modificar algum professor?")
                print("Menu opções de escolha:")
                print("    1 - Sim\n    2 - Não")
                escolha = input("Digite o número da opção: ").lower()
                if escolha == "1" or escolha == "sim":
                    clear()
                    contador = 0
                    print("Os registros existentes até o momento são:")
                    for p in listaProfessores:
                        print("     ",contador," - Professor:", p,"\n           Disciplina:", listaDisciplinas[contador],"\n")
                        contador += 1
                        if contador == len(listaProfessores):
                            break
                    modificar = int(input("Digite o número do professor que deseja modificar: "))
                    for p in range(len(listaProfessores)):
                        if p == modificar:
                            nomeProfessor = input("Digite o nome do professor que deseja cadastrar: ").lower()
                            listaProfessores[p] = (nomeProfessor)
                            nomeDiciplina = input("Digite qual disciplina esse professor leciona: ").lower()
                            listaDisciplinas[p] = (nomeDiciplina)
                            clear()
                            print("     Professor(a) cadastrado com sucesso!")
                            break
                        elif modificar > len(listaProfessores):
                            clear()
                            print("     Professor não encontado ou a opção está inválida!")
                            break
                    break
                elif escolha == "2" or escolha == "não" or escolha == "nao":
                    opcaoModificacao1 = False
                    opcaoModificacao2 = False
                    clear()
                else:
                    clear()
                    print("     Opção inválida!")
    elif comando == "4":
        # bloco de código de verificação dos registros
        opcaoVerificacao1 = True
        opcaoVerificacao2 = True
        while opcaoVerificacao1:
            contador = 0
            print("Os registros existentes até o momento são:")
            for p in listaProfessores:
                print("     ",contador," - Professor:", p,"\n           Disciplina:", listaDisciplinas[contador],"\n")
                contador += 1
                if contador == len(listaProfessores):
                    break
            opcaoVerificacao2 = True
            while opcaoVerificacao2:
                print("Deseja verificar novamente?")
                print("Menu opções de escolha:")
                print("    1 - Sim\n    2 - Não")
                escolha = input("Digite o número da opção: ").lower()
                if escolha == "1" or escolha == "sim":
                    opcaoVerificacao2 = False
                    clear()
                    continue
                elif escolha  == "2" or escolha == "não" or escolha == "nao":
                    opcaoVerificacao1 = False
                    opcaoVerificacao2 = False
                    clear()
                else:
                    clear()
                    print("     Opção inválida!")
    elif comando == "0":
        clear()
        print("        ³\_(õ.Õ)_/³")
        print("PROGRAMA FINALIZADO, ATÉ BREVE!")
        print("CRIADO POR: RAMON / IZABELLA / JOÃO PEDRO © 2022 TRABALHO PROGRAMAÇÃO: TODOS OS DIREITOS RESERVADOS.")
        programa = False
    else:
        clear()
        print("     Opção inválida!")