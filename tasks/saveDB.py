from prefect import Task
from models import Projetos, Vereadores
import json

class SaveDB(Task):

    def run(self,new_projects):
        self.logger.info("Salvando os processos no banco")
        try:
            self.logger.info(f"{new_projects}")
            self.saveDB(new_projects)
            self.logger.info(f"Projetos salvos no banco com sucesso")
        except Exception as err:
            self.logger.error(f"Erro ao salvar os projetos no banco {err}")

    def saveDB(self,new_projects):
        for key in new_projects.keys():
            dados = {"processo" : key,
                     "protocolo" : new_projects[key]["protocolo"],
                     "data" : new_projects[key]["data"],
                     "titulo" : new_projects[key]["resumo"],
                     "situacao" : new_projects[key]["situacao"],
                     "vereador" : new_projects[key]["autor"],
                     "tipo" : new_projects[key]["tipo"] }
            Projetos.insert(dados).execute()

