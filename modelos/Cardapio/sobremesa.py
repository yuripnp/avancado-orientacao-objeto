from modelos.Cardapio.itemCardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tamanho, blend ):
        """
        Inicializa uma nova sobremesa com calorias e blend.
        :param caloria: Calorias da sobremesa.
        :param blend: Blend da sobremesa.
        """
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._blend = blend

    def aplicar_desconto(self):
        pass