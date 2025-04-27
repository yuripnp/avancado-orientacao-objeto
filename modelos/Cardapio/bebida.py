from modelos.Cardapio.itemCardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        """
        Inicializa uma nova bebida com teor alcoólico e volume.
        :param alcoolico: Teor alcoólico da bebida.
        :param volume: Volume da bebida.
        """
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome} - R$ {self._preco:.2f} ({self._volume}ml'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
