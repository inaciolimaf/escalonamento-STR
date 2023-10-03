import pandas as pd
import re

class Task:
    def __init__(self, P, C):
        self.P = P
        self.C = C
    def __str__(self):
        return f"Período:{self.P}, custo de computação: {self.C}"
      
def transformarNumero(numero: str):
    numero = re.findall(r'\d+', numero)[0]
    return int(numero)
def cargaCumulativa(i, tasks: [], ts:[]):
    uList = []
    wList = []
    for t in ts:
        u = 0
        w = 0
        for j in range(0, i):
            w += (t/tasks[j].P)*tasks[j].C
        u = w/t
        if u>1:
            print("A tarefa: {tasks[j]}, no tempo {t} não é escalonável")
        
if __name__ == "__main__":
    tasks = []
    df = pd.read_excel("MCMV - Definições.xlsx")
    df = df.loc[df["Core"]==1]
    df = df.loc[df["Periódica"]=="Sim"]
    for i, line in df.iterrows():
        tempoComputacao = transformarNumero(line["Tempo de Computação"])
        periodo = transformarNumero(line["Período/Deadline"])
        tasks.append(Task(periodo, tempoComputacao))
    for i, task in enumerate(tasks):
        cargaCumulativa(i, tasks, range(1, 201))

        