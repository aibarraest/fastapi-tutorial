# Creation of a FastAPI project
1. Make a directory in your file system.
   ```bash
   mkdir fastapi-tutorial
   ```
2. In your terminal, change your directory into the new directory you made.
   ```bash
   cd fastapi-tutorial
   ```
3. Create a virtual environment for your project to separate dependencies between projects.
    ```bash
    python -m venv .venv # create virtual environment
    source .venv/bin/activate # activate virtual environment
    deactivate # DO NOT RUN YET: deactivates virtual environment
    ```
4. Install FastAPI and uvicorn in your project.
    ```bash
    pip install fastapi uvicorn
    ```
   - A good practice is to have a `requirements.txt` file where everyone who clones the project can see all of the
   dependencies they need to install and their version.
   ```bash
   pip freeze > requirements.txt # to make the requirements.txt with the dependencies needed
   pip install -r requirements.txt # this command replaces `pip install fastapi uvicorn` since it installs everything
   ```
5. Run `uvicorn python-file-name:fastapi-instance-variable --reload` to expose your endpoint locally.
   - The `--reload` flag is used to update your server everytime you save the python file locally.
   ```bash
   uvicorn main:app --reload
   ```
