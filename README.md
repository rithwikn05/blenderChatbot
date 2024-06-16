# Pulling from repo

1. When pulling the code, since the Stable Diffusion folder is a submodule, when pulling from the repo, to retrieve changes specifically to the stable diffusion folders, use this command: git submodule update --remote --merge
2. Now this will pull the changes from the submodule since pulling the repo wont necessarily make changes to the submodule
3. When adding changes to the submodule, first enter the cloned repo and add the changes. Then go out to your repo and add those. When pushing, enter the clone repo and push those first and then move out to your repo and push those.