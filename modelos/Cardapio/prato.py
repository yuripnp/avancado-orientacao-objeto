from modelos.Cardapio.itemCardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao, proteina):
        """
        Inicializa um novo prato com proteína.
        :param proteina: Proteína do prato.
        """
        super().__init__(nome, preco)
        self._descricao = descricao
        self._proteina = proteina

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} - {self._proteina}"
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)