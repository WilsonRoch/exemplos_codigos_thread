import threading


class CaixaCentralizadoModel:
    def __init__(self, saldo_inicial, valor_ficha_reais):
        self.saldo_central = saldo_inicial
        self.valor_ficha_reais = valor_ficha_reais
        self.lock = threading.Lock()

    def registrar_venda(self, quantidade_fichas=1):
        valor_venda = quantidade_fichas * self.valor_ficha_reais
        # dentro desse bloco apenas uma unica thread vai ter acesso, evitando que duas threads alterem o saldo ao mesmo tempo
        with self.lock:
            self.saldo_central += valor_venda
            return self.saldo_central

    def obter_saldo_atual(self):
        # dentro desse também vai acontecer o mesmo, apenas uma thread por vez vai ter acesso ao saldo
        with self.lock:
            return self.saldo_central