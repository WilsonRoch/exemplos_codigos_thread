import threading


class CaixaView:
    def __init__(self):
        self.lock = threading.Lock()

    @staticmethod
    def formatar_real(valor_reais):
        texto = f"R$ {valor_reais:,.2f}"
        return texto.replace(",", "X").replace(".", ",").replace("X", ".")

    def mostrar_tela_inicio(self, quantidade_caixas, vendas_por_caixa, valor_ficha_reais):
        with self.lock:
            print("Sistema de Caixa Centralizado de Evento")
            print(f"Caixas: {quantidade_caixas}")
            print(f"Vendas por caixa: {vendas_por_caixa}")
            print(f"Valor da ficha: {self.formatar_real(valor_ficha_reais)}")
            print("--------------------------------")

    def mostrar_inicio_caixa(self, nome_caixa):
        with self.lock:
            print(f"{nome_caixa} iniciou as vendas.")

    def mostrar_fim_caixa(self, nome_caixa, vendas_realizadas, saldo_parcial_reais):
        with self.lock:
            print(
                f"{nome_caixa} finalizou {vendas_realizadas} vendas. "
                f"Saldo parcial: {self.formatar_real(saldo_parcial_reais)}"
            )

    def mostrar_resumo_final(self, saldo_final_reais, saldo_esperado_reais):
        with self.lock:
            print("-")
            print(f"Saldo final: {self.formatar_real(saldo_final_reais)}")
            print(f"Saldo esperado: {self.formatar_real(saldo_esperado_reais)}")
            print("Resultado:", "OK" if saldo_final_reais == saldo_esperado_reais else "DIVERGENTE")