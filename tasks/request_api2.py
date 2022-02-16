from prefect import Task
import json
import requests
import time

class RequestAPI2(Task):

    def run(self,url,ploads,interval):
        self.logger.info(f"Chamando API: {url}")
        for pload in ploads:
            try:
                self.postRequest(url, pload)
                self.logger.info(f"Esperar {interval} segundos para o prox request")
                time.sleep(interval)
            except Exception as err:
                self.logger.error(f"Erro no request {err}")

    def postRequest(self,url,pload):
        pload = json.loads(pload)
        response = requests.post(url, data=pload)
        self.logger.info(f"Request - {pload} realizado: {response}")
        return response

