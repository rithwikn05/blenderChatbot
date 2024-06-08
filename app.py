from flask import Flask, request, jsonify
from tasks import celery, run_blender_script

def create_app():
    app = Flask(__name__)

    # Flask configuration
    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_RESULT_BACKEND='redis://localhost:6379/0'
    )

    # Route to start a Blender script
    @app.route('/run_blender', methods=['POST'])
    def run_blender():
        data = request.get_json()
        script_path = data.get('script_path')
        result_path = data.get('result_path')

        if not script_path or not result_path:
            return jsonify({'error': 'Please provide script_path and result_path'}), 400

        task = run_blender_script.apply_async(args=[script_path, result_path])
        return jsonify({'task_id': task.id}), 202

    # Route to check task status
    @app.route('/status/<task_id>', methods=['GET'])
    def task_status(task_id):
        task = run_blender_script.AsyncResult(task_id)
        if task.state == 'PENDING':
            response = {
                'state': task.state,
                'current': 0,
                'total': 1,
                'status': 'Pending...'
            }
        elif task.state != 'FAILURE':
            response = {
                'state': task.state,
                'current': 1,
                'total': 1,
                'status': 'Completed',
                'result': task.result
            }
        else:
            response = {
                'state': task.state,
                'current': 1,
                'total': 1,
                'status': str(task.info),
            }
        return jsonify(response)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
