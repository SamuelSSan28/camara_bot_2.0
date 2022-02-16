from prefect import Task
from models import Projetos

class GetLastProcess(Task):

	def run(self):
		self.logger.info("Iniciando metodo para buscar o ultimo processo cadastrado no banco")
		try:
			last_process = self.getLastProcess()
			self.logger.info(f"Últimos processo encontrado {last_process}")
			return last_process

		except (KeyError, TypeError) as err:
			self.logger.error(f"Erro ao buscar o processo" )


	def getLastProcess(self):
		projetos = Projetos.select().order_by(Projetos.processo)
		return projetos[-1].processo

