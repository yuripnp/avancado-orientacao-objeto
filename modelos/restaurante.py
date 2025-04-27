from modelos.Cardapio.itemCardapio import ItemCardapio
from modelos.avaliacao import Avaliacao

class Restaurante:
    """
    Classe que representa um restaurante."""
    restaurantes = []
    def __init__(self, nome, categoria):
        """
        Inicializa um novo restaurante com nome e categoria.
        :param nome: Nome do restaurante.
        :param categoria: Categoria do restaurante.
        """
    
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """"
        Retorna uma representação em string do restaurante."""
        return f"{self.nome} ({self.categoria}) "
    
    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property # é quando eu quero que uma função se comporte como um atributo
    def mostrar_cardapio(self):
        print(f"Cardapio do restaurante {self._nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_tamanho'):
                messagem = f'{i} - {item._nome} : R${item._preco} | {item._tamanho}'
                print(messagem)
            elif hasattr(item, '_descricao'):
                messagem = f'{i} - {item._nome} : R${item._preco} | {item._descricao}'
                print(messagem)
    
    @property # a forma como o atributo é apresentado
    def ativo(self):
        """
        Retorna o status do restaurante (ativo ou inativo).
        :return: '☒' se o restaurante estiver ativo, '☐' caso contrário.
        """
        return '☒' if self._ativo else '☐'
    
    def alternar_ativo(self):
        """
        Alterna o status do restaurante entre ativo e inativo."""
        self._ativo = not self._ativo
    
    
    def receber_avaliacao(self, cliente, nota, comentario):
        """
        Recebe uma avaliação de um cliente.
        :param cliente: Nome do cliente que fez a avaliação.
        :param nota: Nota dada pelo cliente (de 0 a 5).
        :param comentario: Comentário do cliente sobre o restaurante.
        """
        avaliacao = Avaliacao(cliente, nota, comentario)
        self._avaliacoes.append(avaliacao)
    
    @property # é quando eu quero que uma função se comporte como um atributo
    def media_avaliacoes(self):
        """
        Calcula a média das avaliações do restaurante.
        :return: Média das notas das avaliações (de 0 a 5).
        """
        if not self._avaliacoes:
            return "Sem avaliações"
        elif len(self._avaliacoes) == 1:
            return self._avaliacoes[0].nota
        soma = sum(avaliacao.nota for avaliacao in self._avaliacoes)
        return round(soma / len(self._avaliacoes), 1)
    
    @classmethod
    def listar_restaurantes(cls):
        """
        Lista todos os restaurantes cadastrados."""
        for restaurante in cls.restaurantes:
            print(f"Nome: {restaurante._nome.ljust(10)}, Categoria: {restaurante._categoria.ljust(10)} - Ativo: {restaurante.ativo.ljust(10)}, Média: {str(restaurante.media_avaliacoes).ljust(10)}")
