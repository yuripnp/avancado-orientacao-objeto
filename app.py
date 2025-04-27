
from modelos.Cardapio.bebida import Bebida
from modelos.Cardapio.prato import Prato
from modelos.Cardapio.sobremesa import Sobremesa
from modelos.restaurante import Restaurante


restaurante_praca = Restaurante("Praça", "Comida Brasileira")
suco_melancia = Bebida("Suco de Melancia", 6.00, "G")
suco_melancia.aplicar_desconto()
prato_moqueca = Prato("Moqueca", 30.00, "peixe ao caldo", "Peixe")
prato_moqueca.aplicar_desconto()
sorvete = Sobremesa("milkshake", 12.00, "G", "Chocolate")
restaurante_praca.adicionar_item_cardapio(suco_melancia)
restaurante_praca.adicionar_item_cardapio(prato_moqueca)
restaurante_praca.adicionar_item_cardapio(sorvete)


def main():
    restaurante_praca.mostrar_cardapio

if __name__ == "__main__":
    main()