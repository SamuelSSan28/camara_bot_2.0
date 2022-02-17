# coding=utf8
from prefect import Task
import json
import requests
import time
from prefect.engine import signals

class RequestAPI2(Task):

    def run(self,url,ploads,interval):
        self.logger.info(f"Chamando API: {url}")

        if ploads and len(ploads) == 0 or ("err" in str(ploads)):
            raise signals.SKIP("Nenhum projeto encontrado")

        for pload in ploads:
            try:
                response = self.postRequest(url, pload)
                if response and response.status_code == 400:
                    raise signals.FAIL("Erro no request")
                self.logger.info(f"Esperar {interval} segundos para o prox request")
                time.sleep(interval)
            except Exception as err:
                self.logger.error(f"Erro no request {err}")

    def postRequest(self,url,pload):
        pload = json.loads(pload)
        response = requests.post(url, data=pload)
        self.logger.info(f"Request Payload - {pload} realizado: {response}")
        return response

