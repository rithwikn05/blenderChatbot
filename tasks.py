from celery_config import make_celery
from flask import Flask
import subprocess

app = Flask(__name__)
celery = make_celery(app)

@celery.task
def run_blender_script(script_path, result_path):
    result = subprocess.run(['blender', '--background', '--python', script_path, '--render-output', result_path], capture_output=True, text=True)
    return result.stdout, result.stderr
