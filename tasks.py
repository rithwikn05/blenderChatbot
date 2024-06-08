import subprocess
from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery

# Create the Celery instance
celery = make_celery(create_app())

@celery.task
def run_blender_script(script_path, result_path):
    # Use the Blender executable from the extracted Blender archive
    blender_executable = '/path/to/extracted/blender/blender'

    # Run Blender script with the provided paths
    result = subprocess.run([blender_executable, '--background', '--python', script_path, '--render-output', result_path], capture_output=True, text=True)

    return result.stdout, result.stderr
