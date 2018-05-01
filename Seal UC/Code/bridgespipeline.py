#Code to run pipeline on Bridges
#Author: Jake Lewandowski
from radical.entk import Pipeline, Stage, Task, AppManager, ResourceManager
import os

# ------------------------------------------------------------------------------

if os.environ.get('RADICAL_ENTK_VERBOSE') == None:
    os.environ['RADICAL_ENTK_VERBOSE'] = 'INFO'


def generate_pipeline(name, stages):  #generate the pipeline of prediction and blob detection

    # Create a Pipeline object
    p = Pipeline()
    p.name = name


    for s_cnt in range(stages):

        # Create a Stage object
        s = Stage()
        s.name = 'Stage %s'%s_cnt
    if(stage==1)
            # Create Task 1, training
            t = Task()
            t.name = 'my-task1'         
             t.executable = ['sbatch']   # Assign executable to the task   
             # Assign arguments for the task executable
             t.arguments = ['/Code/trainbatch.bat']
    else
            # Create Task 2, 
            t = Task()
            t.name = 'my-task2'         
             t.executable = ['sbatch']   # Assign executable to the task   
             # Assign arguments for the task executable
             t.arguments = ['/Code/predscript.bat']  
         t.download_output_data = ['classified_images'] #Download resuting images
        
             
    s.add_tasks(t)

        # Add Stage to the Pipeline
        p.add_stages(s)

    return p



if __name__ == '__main__':

    p1 = generate_pipeline(name='Pipeline 1', stages=2)

    res_dict = {

            'resource': 'xsede.bridges',
        'username': 'jel203' #username is not currently included in ensemble toolkit,               so an error arises
            'walltime': 10,
            'cores': 1,
            'project': '',
    }

    # Create Resource Manager object with the above resource description
    rman = ResourceManager(res_dict)

    # Create Application Manager
    appman = AppManager()

    # Assign resource manager to the Application Manager
    appman.resource_manager = rman

    # Execute pipeline
    appman.assign_workflow(p1)

    # Run the Application Manager
    appman.run()
