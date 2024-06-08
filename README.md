# blenderChatbot

steps needed to run files:
1. First install docker if not done so
2. Run dockerfile: docker build -t my-blender-app .
3. Run this command: docker run -d -p 5000:5000 -v /home/username/blender-scripts:/blenderChatbot/scripts -v /home/username/blender-results:/blenderChatbot/results my-blender-app
4. Run python.app in another terminal window to start the Flask application
5. 
