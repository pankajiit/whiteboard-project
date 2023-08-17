Create virtual environment:
    python3 -m venv user-api

Activate virtual environment:
    source user-api/bin/activate

Create run.sh shell file
    paste below command on that file
    uvicorn main:app --reload --port 8001

Then run below command
    chmod +x run.sh 
    
Run project
    ./run.sh

Use the below command to install the requirements.txt file if you face any issues
    pip3 install -r requirements.txt 

Use the below command using export installed commands from our project setup
    pip3 freeze >> requirements.txt