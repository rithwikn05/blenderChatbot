import subprocess
from celery import Celery
from BlenderBackend.extensions import create_app, make_celery


# Create the Celery instance
celery = make_celery(create_app())

@celery.task
def run_blender_script(script_path, result_path):
    # Use the Blender executable from the extracted Blender archive
    # blender_executable = '/path/to/extracted/blender/blender'
    container_script_path = '/blenderChatbot/scripts/' + script_path.split('/')[-1]
    container_result_path = '/blenderChatbot/results/' + result_path.split('/')[-1]
    docker_command = [
        'docker', 'exec', 'blender-container',
        'blender', '--background', '--python', container_script_path, '--render-output', container_result_path]

    # Run Blender script with the provided paths
    result = subprocess.run(docker_command, capture_output = True, text = True)

    return result.stdout, result.stderr
