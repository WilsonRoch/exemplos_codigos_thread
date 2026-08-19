from controller import RelatorioVendasController
from model import RelatorioVendasModel
from view import RelatorioVendasView
import random


def main():
    registros_por_filial = 10000
    
    vendas_por_filial = [
        [random.randint(10, 100) for _ in range(registros_por_filial)]
        for _ in range(4)
    ]

    model = RelatorioVendasModel()
    view = RelatorioVendasView()
    controller = RelatorioVendasController(model, view, vendas_por_filial)
    controller.executar()


if __name__ == "__main__":
    main()
