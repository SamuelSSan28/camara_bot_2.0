from prefect import Task
import json
import requests

class RequestAPI(Task):

    def run(self,url,pload,ploadIsSTR):
        self.logger.info(f"Chamando API: {url}")
        try:
            response = self.postRequest(url,pload,ploadIsSTR)
            self.logger.info(f"Request realizado: {response}")
            return response.text
        except Exception as err:
            self.logger.error(f"Erro no request {err}")

    def postRequest(self,url,pload,ploadIsSTR):
        if ploadIsSTR:
            pload = json.loads(pload)
        reponse = requests.post(url, data=pload)
        return reponse

