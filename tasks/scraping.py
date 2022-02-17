from prefect import Task
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from prefect.engine import signals
from dotenv import dotenv_values

class ScrapingPage(Task):

    def run(self,last_project):
        self.logger.info("Iniciando o scraping dos projetos no site da camara")
        try:
            env_values = dotenv_values(".env")
            MY_SO = env_values['MY_SO']
            projects =  self.scrapingPage(last_project,MY_SO)
            self.logger.info(f"Spraping realizado com sucesso. Projetos encontrados: {projects}")
            return projects
        except Exception as err:
            self.logger.error(f"Erro no scraping {err}")
            raise signals.FAIL("Error: " + err)

    def scrapingPage(self, last_project,MY_SO):
        page = 0
        projetos = []
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        driver = None
        if MY_SO == "WIN":
            driver = webdriver.Chrome('./chromedriver.exe', options=options)
        elif MY_SO == "LINUX":
            driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

        driver.set_page_load_timeout(10000)

        self.logger.info("Faz request")
        driver.get("http://www.splonline.com.br/cmteresina/consulta-producao.aspx")

        while True:
            for i in range(2, 12):
                autores = []
                endereco_processo = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[1]'
                processo = driver.find_element_by_xpath(endereco_processo).text.split(": ")[1]
                autores = []

                if processo == last_project:
                    driver.close()
                    return projetos

                endereco_tipo = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[1]/strong/a'
                tipo = driver.find_element_by_xpath(endereco_tipo).text

                if ("Indicação" in tipo):
                    continue

                self.logger.info(f"Scraping do processo: {processo}")

                endereco_protocolo = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[2]'
                protocolo = driver.find_element_by_xpath(endereco_protocolo).text.split("º ")[1]
                endereco_data = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[3]'
                data = driver.find_element_by_xpath(endereco_data).text.split(": ")[1].split(" ")[0]
                endereco_situacao = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[4]'
                situacao = driver.find_element_by_xpath(endereco_situacao).text.split(": ")[1]
                endereco_autor = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[6]'
                autor = driver.find_element_by_xpath(endereco_autor).text.split(": ")[1]
                aux = autor.split(", ")

                for u in aux:
                    autores.append(u)

                endereco_resumo = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[7]'
                resumo = driver.find_element_by_xpath(endereco_resumo).text
                endereco_setor = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[8]'
                setor = driver.find_element_by_xpath(endereco_setor).text.split(": ")[1]
                endereco_fase = '//*[@id="tabela"]/tbody/tr[' + str(i) + ']/td/div[9]'
                fase = driver.find_element_by_xpath(endereco_fase).text.split(": ")[1]

                projetos.append({"protocolo": protocolo, "tipo": tipo, "data": data, "situacao": situacao,
                                            "autor": autor, "resumo": resumo, "setor": setor, "fase": fase,
                                            "autores": autores,"processo":processo})
            if page < 6:
                page += 1

            pagina_button = '//*[@id="ContentPlaceHolder1_rptPaging_lbPaging_' + str(page) + '"]'
            button = driver.find_element_by_xpath(pagina_button)
            button.click()
            time.sleep(5)


