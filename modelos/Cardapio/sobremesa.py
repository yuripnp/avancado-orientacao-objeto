from modelos.Cardapio.itemCardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    def __init__(self, caloria, blend ):
        """
        Inicializa uma nova sobremesa com calorias e blend.
        :param caloria: Calorias da sobremesa.
        :param blend: Blend da sobremesa.
        """
        self._caloria = caloria
        self._blend = blend