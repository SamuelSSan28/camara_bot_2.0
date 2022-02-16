import datetime
from prefect import Flow, unmapped,task
from getLastProcess import GetLastProcess
from scraping import ScrapingPage
from saveDB import SaveDB
from request_api import RequestAPI
from request_api2 import RequestAPI2

flow = Flow("Camara_Bot")
get_last_process_task = GetLastProcess(name="GetLastProcess")
scraping_projects = ScrapingPage(name="ScrapingPage", max_retries=3, retry_delay=datetime.timedelta(minutes=10))
save_project_sqlite = SaveDB(name="SaveDB")
request_api_1 = RequestAPI(name="Request API")
request_api_2 = RequestAPI2(name="Request API 2")

flow.set_dependencies(scraping_projects,
                      upstream_tasks=[get_last_process_task],
                      keyword_tasks={"last_project": get_last_process_task})

flow.set_dependencies(request_api_1, keyword_tasks={"pload":scraping_projects,
                                                  "url":unmapped("http://localhost:3000/gerar_imagem")}, mapped=True)

flow.set_dependencies(request_api_2, keyword_tasks={"ploads":request_api_1,
                                                  "url":unmapped("http://localhost:3000/postar"),
                                                  "interval":300})

flow.set_dependencies(save_project_sqlite, keyword_tasks={"new_projects":scraping_projects})

if __name__ == '__main__':
    flow.run()