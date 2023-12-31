import pandas as pd
import re
from typing import List


class Task:
    def __init__(self, P: int, C: int):
        self.P = P
        self.C = C

    def __str__(self):
        return f"Período:{self.P}, custo de computação: {self.C}"


def transformarNumero(numero: str):
    numero = re.findall(r'\d+', numero)[0]
    return int(numero)


def cargaCumulativa(i: int, tasks: List[Task], ts: List[int]):
    for t in ts:
        u = 0
        w = 0
        for j in range(0, i):
            w += (t/tasks[j].P)*tasks[j].C
        u = w/t
        if u > 1:
            print(f"No tempo {t} não é escalonável")
            return True


if __name__ == "__main__":
    NUM_CORES = 3
    for i in range(1, NUM_CORES+1):    
        tasks = []
        df = pd.read_excel("MCMV - Definições.xlsx")
        df = df.loc[df["Core"] == i]
        df = df.loc[df["Periódica"] == "Sim"]
        for _, line in df.iterrows():
            tempoComputacao = transformarNumero(line["Tempo de Computação"])
            periodo = transformarNumero(line["Período = Deadline"])
            tasks.append(Task(periodo, tempoComputacao))
        escalonavel = True
        for j, task in enumerate(tasks):
            if cargaCumulativa(j+1, tasks, range(1, 10001)):
                escalonavel = False
                break
        if escalonavel:
            print(f"As tarefas são escalonáveis para o core {i}")
