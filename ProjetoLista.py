from ListaFuncoes import * 

print ("\n LISTA DE TAREFAS")
while True:
    print("\nMenu:")
    print("1.Adicinar uma NOVA TAREFA")
    print("2. Visualizar tarefas PENDENTES")
    print("3. Visualizar por PRIORIDADES")
    print("4. Visualizar tarefas FINALIZADAS")
    print("5. Visualizar todas as TAREFAS")
    print("6. Marcar tarefa como CONCLUÍDA")
    print("7. REMOVER alguma TAREFA")
    print("8. Fechar lista de tarefas")
    opcao = input ("\n Digite o número correspondente no que deseja realizar: ")
     
    if opcao=="1":
        print("\nAdicionar uma tarefa:")
        tarefanome = input("Insira o nome da tarefa: ")
        tipotarefa = input("Insira a categoria: ")
        descricaotarefa = input("Descrição: ")
        priotarefa = input("Insira a prioridade(normal, importante ou urgente):  ").upper()
        addtarefa(tarefanome,tipotarefa,descricaotarefa,priotarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
       print("\n LISTA DE TAREFAS PENDENTES:")
       pendentes( )     
    elif opcao == "3":
        prioridade = input("Digite o tipo de prioridade que desejar visualizar (normal, importante ou urgente): ").upper()
        print(f"\n LISTA DE TAREFAS {prioridade.upper()}:")
        prioridades(prioridade)
    elif opcao == "4":
        print("\n LISTA DE TAREFAS FINALIZADAS:" )
        finalizadas( )
        
    elif opcao == "5":
        print("\n LISTA DE TAREFAS:")
        listartarefas( )
    elif opcao=="6":
        print("\n LISTA DE TAREFAS:")
        listartarefas( )
        marcartarefa = int(input("\n Para marcar uma tarefa como concluida digite o seu indice,ou digite '0'(zero) para voltar pro menu príncipal: ")) 
        concluitarefa(marcartarefa)
    elif opcao=="7":
        if not tarefas:
            print ("\nNenhuma tarefa registrada.")
        else:
         print("\n Lista de tarefas: ")
         listartarefas( )
         tarefaremovida = int(input("Digite o número da tarefa que deseja remover: "))
         remover(tarefaremovida)
    elif opcao == "8":
       break 
    else:
        print("\nOpção inválida! Por favor, escolha uma opção válida. ") 






    

 







