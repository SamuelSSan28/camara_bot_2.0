from prefect import Flow
from prefect.executors import LocalExecutor

from getLastProcess import GetLastProcess

with Flow("Camara_Bot_Flow") as flow:

    get_last_process_task = GetLastProcess()
    flow.add_task(get_last_process_task)
    
    result1 = get_last_process_task.run()
    
    state = flow.run()

    assert state.is_successful()


flow.register(project_name="second")

        
            
                           
