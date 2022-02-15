from prefect import Flow
from prefect.executors import LocalExecutor

from getLastProcess import GetLastProcess
from project2json import Projects2Json

with Flow("Camara_Bot_Flow") as flow:

    get_last_process_task = GetLastProcess()
    save_project_2_json = Projects2Json()

    flow.add_task(get_last_process_task)
    
    last_process = get_last_process_task.run()

    new_projects = []

    save_project_2_json.run(new_projects)
    
    state = flow.run()

    assert state.is_successful()


#flow.register(project_name="second")

        
            
                           
