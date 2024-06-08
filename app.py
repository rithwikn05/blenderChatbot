from flask import Flask, request, jsonify, send_file
from tasks import run_blender_script
import os
import uuid

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

UPLOAD_FOLDER = '/tmp/uploads'
RESULTS_FOLDER = '/tmp/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

@app.route('/run_blender_script', methods=['POST'])
def handle_script():
    script = request.files['script']
    script_filename = f"{uuid.uuid4()}_{script.filename}"
    script_path = os.path.join(UPLOAD_FOLDER, script_filename)
    script.save(script_path)

    result_filename = f"{uuid.uuid4()}_result.png"
    result_path = os.path.join(RESULTS_FOLDER, result_filename)

    task = run_blender_script.apply_async(args=[script_path, result_path])
    return jsonify({'task_id': task.id, 'status': 'Processing'})

@app.route('/task_status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = run_blender_script.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'result': task.result
        }
        if task.state == 'SUCCESS':
            response['file'] = task.result[1]
    else:
        response = {
            'state': task.state,
            'status': str(task.info)
        }
    return jsonify(response)

@app.route('/download_result/<filename>', methods=['GET'])
def download_result(filename):
    return send_file(os.path.join(RESULTS_FOLDER, filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
