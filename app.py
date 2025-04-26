
from modelos.Cardapio.bebida import Bebida
from modelos.Cardapio.prato import Prato
from modelos.restaurante import Restaurante


restaurante_praca = Restaurante("Praça", "Comida Brasileira")
suco_melancia = Bebida(False, "300ml", "Suco de Melancia", 5.00)
prato_moqueca = Prato("Peixe", "Moqueca", 25.00)

def main():
    pass

if __name__ == "__main__":
    main()