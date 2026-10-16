class Playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def set_id(self,id):
        if id <= 0 : raise ValueError("O id precisa ser maior que zero.")
        self.__id=id

    def set_nome(self,nome):
        if nome == "": raise ValueError("O nome deve ser informado.")
        self.__nome=nome

    def set_descricao(self,descricao):
        if descricao == "": raise ValueError("A descrição deve ser informada.")

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def TempoTotal():
        pass

    def __str__(self):
        pass

class PlaylistItem:
    pass

class Musica:
    pass

class UI:
    playlists=[]
    playlistitens=[]
    musicas=[]