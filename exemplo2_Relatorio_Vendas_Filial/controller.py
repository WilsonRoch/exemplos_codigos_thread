import threading


class RelatorioVendasController:
	def __init__(self, model, view, vendas_por_filial):
		self.model = model
		self.view = view
		self.vendas_por_filial = vendas_por_filial
		self.resultados_filiais = [0] * len(vendas_por_filial)
		self.threads = []

	def executar(self):
		self.view.mostrar_tela_inicio(
			quantidade_filiais=len(self.vendas_por_filial),
			registros_por_filial=len(self.vendas_por_filial[0]),
		)

		for indice_filial, vendas_filial in enumerate(self.vendas_por_filial):
			thread = threading.Thread(
				target=self._processar_filial,
				args=(indice_filial, vendas_filial),
				name=f"Filial {indice_filial + 1}",
			)
			self.threads.append(thread)
			thread.start()

		for thread in self.threads:
			thread.join()

		total_geral = sum(self.resultados_filiais)
		self.view.mostrar_resumo_final(self.resultados_filiais, total_geral)

	def _processar_filial(self, indice_filial, vendas_filial):
		self.resultados_filiais[indice_filial] = self.model.somar_vendas(vendas_filial)
