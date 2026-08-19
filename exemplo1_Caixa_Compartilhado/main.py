from controller import CaixaController
from model import CaixaCentralizadoModel
from view import CaixaView


def main():
    quantidade_caixas = 5
    vendas_por_caixa = 1000
    saldo_inicial = 0
    valor_ficha_reais = 10

    model = CaixaCentralizadoModel(
        saldo_inicial=saldo_inicial,
        valor_ficha_reais=valor_ficha_reais,
    )
    view = CaixaView()
    controller = CaixaController(
        model,
        view,
        quantidade_caixas=quantidade_caixas,
        vendas_por_caixa=vendas_por_caixa
    )
    controller.executar()


if __name__ == "__main__":
    main()