# MLFlow_Tutorial 

## workflows 

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in the src config
6. update the components
7. Update the pipeline
8. Update the main.yaml
9. Update the dvc.yaml
    


Clone the repository

'''bash
https://dagshub.com/Sengarofficial/MLFlow_Tutorial
'''

### STEP 01 - Create a conda environment after opening the repository 

'''bash
conda create -n mlproj python=3.8 -y
'''

'''bash
conda activate mlproj
'''

### STEP 02- install the requirements
'''bash
pip install -r requirements.txt
'''

'''bash
# Finally run the following command
python app.py
'''
Now, 
'''bash
open up you local host and port 
'''

## MLFLOW 

[Documentation](https://https://mlflow.org/docs/latest/index.html)

### cmd 
- mlflow ui


### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Sengarofficial/MLFlow_Tutorial.mlflow \
MLFLOW_TRACKING_USERNAME=Sengarofficial \
MLFLOW_TRACKING_PASSWORD=your_token  \
python script.py

Run this to export as env variables:

'''bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Sengarofficial/MLFlow_Tutorial.mlflow \

export MLFLOW_TRACKING_USERNAME=Sengarofficial \

export MLFLOW_TRACKING_PASSWORD=your_token  \

'''


AWS CICD Deployment With Github Actions 
1. Login to aws console.
2. Create IAM user for the deployment
# with specific access 
1. EC2 Access : It is virtual machine.
2. ECR : Elastic Container registry to save your docker image in aws.


# Description : About the deployment 

1. Build docker image of the source code.
2. Push your docker image to ECR.
3. Launch your EC2.
4. Pull your image from ECR in EC2.
5. Launch your docker image.

#Policy
1. AmazonEC2ContainerRegistryFullaccess
2. AmazonEC2FullAccess 


3. Create ECR repo to store/save docker image 

- Save the URL: 

4. Create EC2 machine (Ubuntu)

5. Open EC2 and install docker in EC2 Machine:

#optional 

sudo apt-get update -y
sudo apt-get upgrade 
