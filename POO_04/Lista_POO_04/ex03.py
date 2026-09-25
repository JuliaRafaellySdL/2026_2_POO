class Cliente:
    def __init__(self,nome,cpf,limite,socio):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_limite(limite)
        self.set_socio=None

    #SETS

    def set_nome(self,nome):
        if nome=="":raise ValueError("O nome deve ser informado")
        self.__nome=nome
    def set_cpf(self,cpf):
        if cpf=="":raise ValueError("O CPF deve ser informado")
        self.__cpf=cpf
    def set_limite(self,limite):
        if limite<0: raise ValueError("O limite de crédito deve ser positivo")
        self.__limite=limite

    def set_socio(self,c):
        self.__socio=c
        c.__socio=self

    #GETS

    def get_nome(self):return self.__nome
    def get_cpf(self):return self.__cpf
    def get_limite(self): return self.__limite

    def get_socio(self): return self.__socio

    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__limite:.2f}"

c1=Cliente("Braúlio","123456",1000)
c2=Cliente("Jorgiano","654321", 2000)
c1.set_socio(c2)
print(c1, c1.get_socio())
print(c2, c2.get_socio())