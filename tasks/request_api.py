from prefect import Task
from prefect.engine import signals
import requests

class RequestAPI(Task):

    def run(self,url,pload):
        self.logger.info(f"Chamando API: {url}")
        try:
            response = self.postRequest(url,pload)
            self.logger.info(f"Request realizado: {response}")

            if response and response.status_code == 400:
                raise signals.FAIL("Erro no request")

            return response.text
        except Exception as err:
            self.logger.error(f"Erro no request {err}")

    def postRequest(self,url,pload):
        reponse = requests.post(url, data=pload)
        return reponse

