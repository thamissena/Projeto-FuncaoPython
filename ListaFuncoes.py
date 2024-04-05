tarefas = [ ]

def addtarefa(nome, categoria, descricao , prioridade):
    tarefas.append ({'nome':nome, 'categoria': categoria, 'descricao':descricao, 'prioridade': prioridade, 'completada': False})
    
   
def listartarefas( ): 
  if not tarefas: 
     print ("\nNenhuma tarefa registrada.")
  else:   
    for indice, tarefa in enumerate(tarefas):
      print(f"{indice +1}. {tarefa['nome']} ({tarefa['categoria']} - Prioridade: {tarefa['prioridade']}): {tarefa['descricao']}. - {'Concluída.' if tarefa['completada'] else 'Pendente.'}")      

def pendentes( ):
  tarefaspendentes = [ tarefa for tarefa in tarefas if tarefa['completada'] == False ]
  if not tarefaspendentes: 
    print ("\nNenhuma tarefa registrada.")
  else:
    for indice, tarefa in enumerate(tarefaspendentes):
      print (f"{indice +1}. {tarefa['nome']} ({tarefa['categoria']} - Prioridade: {tarefa['prioridade']}): {tarefa['descricao']}. - {'Concluída.' if tarefa['completada'] else 'Pendente.'}")  
    

def prioridades(tipoprioridade):
    tarefasprioridades = [tarefa for tarefa in tarefas if tarefa['prioridade']== tipoprioridade]
    if not tarefasprioridades: 
     print ("\nNenhuma tarefa com essa prioridade.")
    else:
     for indice, tarefa in enumerate(tarefasprioridades):
      print (f"{indice +1}. {tarefa['nome']} ({tarefa['categoria']} - Prioridade: {tarefa['prioridade']}): {tarefa['descricao']}. - {'Concluída.' if tarefa['completada'] else 'Pendente.'}")

def concluitarefa(indtarefa):
    if 0 < indtarefa <= len(tarefas):
       tarefas[indtarefa - 1]['completada'] = True
       print("Tarefa concluida com sucesso!")
    else:
       print("\n Tarefa não encontrada.")  
 
def finalizadas( ): 
  tarefasfinalizadas = [ tarefa for tarefa in tarefas if tarefa['completada'] == True ]
  if not tarefasfinalizadas: 
    print ("\nNenhuma tarefa registrada.")
  else:  
    for indice, tarefa in enumerate(tarefasfinalizadas):
      print (f"{indice +1}. {tarefa['nome']} ({tarefa['categoria']} - Prioridade: {tarefa['prioridade']}): {tarefa['descricao']}. - {'Concluída.' if tarefa['completada'] else 'Pendente.'}")
      ntarefa = int(input("\n Para desmarcar uma tarefa como concluida digite o seu indice, ou digite '0'(zero) para voltar pro menu príncipal: ")) 
      desmarcartarefa(ntarefa)

def desmarcartarefa(indtarefa):
    if 0 < indtarefa <= len(tarefas):
      tarefas[indtarefa - 1]['completada'] = False
      print("Tarefa marcada como pendente novamente!")
    else:
      print("\n Tarefa não encontrada.")  


def remover(tarefaremovida):
    if 0 < tarefaremovida <= len(tarefas):
        del tarefas[tarefaremovida-1]
        print("\n Tarefa removida!")
    else:
     print("\n Tarefa não encontrada.")