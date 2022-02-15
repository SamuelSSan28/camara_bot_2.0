from prefect import Task
import sys
import json

class Projects2Json(Task):

    def run(self,new_projects):
        self.logger.info("Salvando os processos em um arquivo JSON")
        try:
            self.saveJson(new_projects)
            self.logger.info(f"JSON salvo com sucesso")
        except Exception as err:
            self.logger.error(f"Erro ao salvar o json {err}")

    def saveJson(self,new_projects):
        new_dict = dict(sorted(new_projects.items()))
        with open("../last_scraping.json", "w", encoding='utf-8') as outfile:
            json.dump(new_dict, outfile, ensure_ascii=False)

