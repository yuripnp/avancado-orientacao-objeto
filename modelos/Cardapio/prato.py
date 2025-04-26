from modelos.Cardapio.itemCardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, proteina, nome, preco):
        """
        Inicializa um novo prato com proteína.
        :param proteina: Proteína do prato.
        """
        super().__init__(nome, preco)
        self._proteina = proteina

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"