import enum
from datetime import datetime, timedelta

class SituacaoEstagio(enum.Enum):
    Cadastrado=1
    Iniciado=2
    Cancelado=3
    Finalizado=4

class Estagio:
    def __init__(self,est,emp):
        self.set_estagiario(est)
        self.set_empresa(emp)
        self.__data_inicio=None
        self.__data_cancelamento=None
        self.__data_fim=None
        self.__situacao=SituacaoEstagio.Cadastrado

    def set_estagiario(self,est):
        if est == "": raise ValueError("Estagiário deve ser informado")
        self.__estagiario=est

    def set_empresa(self,emp):
        if emp == "": raise ValueError("Empresa deve ser informada")
        self.__empresa=emp

    def get_estagiario(self): return self.__estagiario
    def get_empresa(self): return self.__empresa

    def Iniciar(self, data):
        if self.__situacao !=SituacaoEstagio.Cadastrado: raise ValueError("Só é possível iniciar um estágio cadastrado")
        self.__data_inicio=data
        self.__situacao=SituacaoEstagio.Iniciado

    def Cancelar(self, data):
        if self.__situacao == SituacaoEstagio.Finalizado: raise ValueError("Só é possível cancelar um estágio não finalizado")
        self.__data_cancelamento=data
        self.__situacao=SituacaoEstagio.Cancelado

    def Finalizar(self,data):
        if self.__situacao !=SituacaoEstagio.Iniciado: raise ValueError("Só é possível finalizar um estágio iniciado")
        self.__data_fim=data
        self.__situacao=SituacaoEstagio.Finalizado

    def Tempo_estagio(self):
        if self.__situacao==SituacaoEstagio.Cadastrado: return timedelta(0)
        if self.__situacao==SituacaoEstagio.Iniciado: return datetime.now().date() - self.__data_inicio.date()
        if self.__situacao==SituacaoEstagio.Cancelado: return self.__data_cancelamento - self.__data_inicio
        if self.__situacao==SituacaoEstagio.Finalizado: return self.__data_fim - self.__data_inicio
        return self.__data_fim - self.__data_inicio

    def __str__(self):
        s=f"{self.__estagiario} - {self.__empresa}"
        if self.__situacao == SituacaoEstagio.Cadastrado: return s + f" - aguardadndo inicio"
        if self.__situacao == SituacaoEstagio.Iniciado: return s + f" - iniciado em {self.__data_inicio.strftime('%d/%m/%Y')}"
        if self.__situacao == SituacaoEstagio.Cancelado: return s + f" - realizado no período {self.__data_inicio.strftime('%d/%m/%Y')} a {self.__data_cancelamento.strftime('%d/%m/%Y')}"
        if self.__situacao == SituacaoEstagio.Finalizado: return s + f" - realizado no período {self.__data_inicio.strftime('%d/%m/%Y')} a {self.__data_fim.strftime('%d/%m/%Y')}"

"""
a=Estagio("Pedro", "IFRN")
b=Estagio("Lucas","UFRN")
c=Estagio("Danielle","INSS")
d=Estagio("Marília", "Serpro")

print(a)
print(b)
print(c)
print(d)


a.iniciar(datetime(2026,3,1))
print(a)
print(a.tempo_estagio)
"""

class UI:
    estagios=[]

    @staticmethod
    def main():
        op=0
        while op != 9:
            op= UI.menu()
            if op == 1: UI.Inserir()
            if op == 2: UI.listar_empresa()
            if op == 3: UI.listar_estagiario()
            if op == 4: UI.filtrar_situacao()
            if op == 5: UI.iniciar_estagio()

    @staticmethod
    def menu():
        print("1 - Inserir, 2 - Listar ordenado por empresa, 3 - Listar estagiário, 4 - Filtrar por situação, 5 - Iniciar estágio, 9 - Fim")
        return int(input("Informe a opção: "))

    @classmethod
    def Inserir(cls):
        estagiario=input("Informe o nome de estagiário: ")
        empresa=input("Informe o nome da empresa: ")
        x=Estagio(estagiario,empresa)
        cls.estagios.append(x)

    @classmethod
    def listar_empresa(cls):
        cls.estagios.sort(key= lambda x: x.get_empresa() + x.get_estagiario())
        for x in cls.estagios:
            print(x)

    @classmethod
    def listar_estagiario(cls):
        cls.estagios.sort(key= lambda x: x.get_estagiario()) 
        for x in cls.estagios:
            print(x)

    @classmethod
    def filtrar_situacao(cls):
        op= int(input("Informe a situação: 1 - Cadastrado, 2 - Iniciado, 3 - Cancelado, 4 - Finalizado"))
        r=[]
        for x in cls.estagios:
            if x.get_situacao() == SituacaoEstagio(op): r.append(x)
        for x in r:
            print(x)

    @classmethod
    def iniciar_estagio(cls):
        for i,x in cls.estagios:
            if x.get_situacao() == SituacaoEstagio.Cadastrado:print(i, ":",x)
        op=int(input("Informe o número do estágio para iniciar: "))
        cls.estagios[op].Iniciar(datetime.now())


UI.main()

'''
def func(x):
    return x*x

f= func
g= lambda x: x**3

print(func(4))
print(f(5))
print(g(4))
'''