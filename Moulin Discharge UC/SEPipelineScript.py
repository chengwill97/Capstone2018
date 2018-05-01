#Code to run StreamExtraction Pipeline on Bridges

from radical.entk import Pipeline, Stage, Task, AppManager, ResourceManager
import os

# ------------------------------------------------------------------------------

if os.environ.get('RADICAL_ENTK_VERBOSE') == None:
	os.environ['RADICAL_ENTK_VERBOSE'] = 'INFO'


def generate_pipeline(name, stages):  #Generate Pipeline for Stream Extraction/Morphological Thinning
    
    # Create a Pipeline object
    p = Pipeline()
    p.name = 'p1'

    for s_cnt in range(stages):
        
    # Create a Stage object, Stream Extraction
    s1 = Stage()
    s1.name = ‘Stage 1’

    # Create a Stage object, Morphological Thinning
    s2 = Stage()
    s2.name = ‘Stage 2’

    
    # Create Task 1, Stream Extraction
    t1 = Task()
    t1.name = 'Task 1'
    t1.executable = ['sbatch']   # Assign executable to the task
    t1.arguments = ['$SCRATCH/ashk96/StreamExtraction.bat'] # Assign arguments for the StreamExtraction

    # Add Task 1 to Stage 1
    s1.add_tasks(t1)
    
    # Add Stage 1 to the Pipeline
    p.add_stages(s1)
   
    # Create Task 2, Morphological Thinning
    t2 = Task()
    t2.name = 'Task 2'
    t2.executable = ['sbatch']   # Assign executable to the task
    t2.arguments = ['$SCRATCH/ashk96/Thin_Multi.bat'] # Assign arguments for the task executable
                    

    # Add Task 2 to Stage 2
    s2.add_tasks(t2)
    
    # Add Stage 2 to the Pipeline
    p.add_stages(s2)

    return p


if __name__ == '__main__':
    
      
    p1 = generate_pipeline(name='Stream Extraction', stages=2)
    res_dict = {
        
            'resource': 'xsede.bridges',
            'walltime': 02:00:00,
            'cores': 2,
            'project': 'TG-MCB090174',
            'queue': '',
            'schema': 'ssh'

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
