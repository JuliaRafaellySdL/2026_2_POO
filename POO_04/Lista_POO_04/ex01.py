class Musica:
    def __init__(self,titulo,artista,album):
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)

    def set_titulo(self,titulo):
        if titulo == "": raise ValueError("Título deve ser informado")
        self.__titulo=titulo
    def set_artista(self,artista):
        if artista == "": raise ValueError("Artista deve ser informado")
        self.__artista=artista
    def set_album(self,album):
        if album == "": raise ValueError("Álbum deve ser informado")
        self.__album=album

    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def __str__(self):
        return f"{self.__titulo} - {self.__artista} - {self.__album}"

class Playlist:
    def __init__(self, nome, descricao):
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.__musicas=[]
    def set_nome(self,nome):
        if nome=="": raise ValueError("Nome deve ser informado")
        self.__nome=nome
    def set_descricao(self,descricao):
        if descricao=="": raise ValueError("Descrição deve ser informada")
        self.__descricao=descricao

    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao

    def inserir(self,m):
        self.__musicas.append(m)
    def listar(self):
        return self.__musicas
    def __str__(self):
        return f"A playlist {self.__nome} tem {len(self.__musicas)} músicas(s)"

p=Playlist("Nacionais", "Preferidas")
x=Musica("Contrução","Chico Buarque","Construção")
y=Musica("Easy", "Ivete Sangalo", "Ao Vivo")

p.inserir(x)
p.inserir(y)

print(p)
for m in p.listar():
    print("     ", m)