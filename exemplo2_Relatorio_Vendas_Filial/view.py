class RelatorioVendasView:
	@staticmethod
	def mostrar_tela_inicio(quantidade_filiais, registros_por_filial):
		print("Processamento de Relatorio de Vendas por Filial")
		print(f"Filiais: {quantidade_filiais}")
		print(f"Registros por filial: {registros_por_filial}")
		print("--------------------------------")

	@staticmethod
	def mostrar_resumo_final(resultados_filiais, total_geral):
		for indice_filial, total_filial in enumerate(resultados_filiais, start=1):
			print(f"Filial {indice_filial}: {total_filial}")

		print("-")
		print(f"Total geral: {total_geral}")
