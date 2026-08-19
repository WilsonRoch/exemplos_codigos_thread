import threading


class CaixaController:
    def __init__(self, model, view, quantidade_caixas, vendas_por_caixa):
        self.model = model
        self.view = view
        self.quantidade_caixas = quantidade_caixas
        self.vendas_por_caixa = vendas_por_caixa
        self.threads = []

    def executar(self):
        """
        Executa o fluxo principal do sistema de caixa centralizado. Chama a view para mostrar a tela inicial,
        cria e inicia as threads de cada caixa usando o metodo _vender,
        aguarda a finalização das threads e exibe o resumo final do saldo.
        """
        saldo_esperado_reais = self.quantidade_caixas * self.vendas_por_caixa * self.model.valor_ficha_reais

        self.view.mostrar_tela_inicio(
            self.quantidade_caixas,
            self.vendas_por_caixa,
            self.model.valor_ficha_reais,
        )

        # Cria e inicia as threads de cada caixa
        for indice_caixa in range(1, self.quantidade_caixas + 1):
            nome_caixa = f"Caixa {indice_caixa}"
            thread = threading.Thread(
                target=self._vender,
                args=(nome_caixa,),
                name=nome_caixa,
            )
            self.threads.append(thread)
            thread.start()

        # Aguarda a finalização de todas as threads
        for thread in self.threads:
            thread.join()

        saldo_final_reais = self.model.obter_saldo_atual()
        self.view.mostrar_resumo_final(saldo_final_reais, saldo_esperado_reais)

    def _vender(self, nome_caixa):
        """
        Simula o processo de vendas em cada caixa. Mostra o início das vendas, registra as vendas no model e exibe o saldo parcial após cada venda.
        """
        self.view.mostrar_inicio_caixa(nome_caixa)

        saldo_parcial_reais = self.model.obter_saldo_atual()
        for _ in range(self.vendas_por_caixa):
            saldo_parcial_reais = self.model.registrar_venda()

        self.view.mostrar_fim_caixa(nome_caixa, self.vendas_por_caixa, saldo_parcial_reais)