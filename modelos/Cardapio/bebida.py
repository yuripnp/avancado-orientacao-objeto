
from modelos.Cardapio.itemCardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, alcoolico, volume, nome, preco):
        """
        Inicializa uma nova bebida com teor alcoólico e volume.
        :param alcoolico: Teor alcoólico da bebida.
        :param volume: Volume da bebida.
        """
        super().__init__(nome, preco)
        self._alcoolico = (alcoolico)
        self._volume = volume

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} ({self._volume}ml)"