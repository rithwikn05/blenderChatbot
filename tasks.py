from celery import Celery

def make_celery():
    celery = Celery(
        'tasks',
        backend='redis://localhost:6379/0',
        broker='redis://localhost:6379/0'
    )
    return celery

celery = make_celery()

@celery.task
def run_blender_script(script_path, result_path):
    result = subprocess.run(['blender', '--background', '--python', script_path, '--render-output', result_path], capture_output=True, text=True)
    return result.stdout, result.stderr
