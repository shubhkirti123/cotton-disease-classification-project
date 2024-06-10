# Cotton Plant Disease Classification Web Application

## Problem Statement
Diseases found in Agricultural crops are a major threat that causes production and economic losses as well as
reduction in both quality and quantity of agricultural products. In India, 70% of the population depends on
agriculture which contributes about 17% of the total GDP of our country. Cotton is a very important cash crop
in India. Farmers have difficulty switching from one disease control policy to another. It is difficult for the
human eye to identify the exact type of leaf disease that occurs on the plant leaves, which also requires constant
monitoring of experts, which can be prohibitively expensive on large farms.
Expert naked eye observation is the
main approach adopted and used in practice to detect plant diseases. With the help of the Deep CNN model, we
can use images processing techniques to analyze dead leaf images and extract the features such as color,
texture, and other characteristics. 

The aim is to develop algorithms and techniques based on images of leaves or other plant features that can automatically detect
and classify agricultural plant diseases. This can help farmers to assist and manage the disease.

## Dataset
The dataset is downloaded from [Kaggle](https://www.kaggle.com/janmejaybhoi/cotton-disease-dataset). and total size is 152 MB. The dataset contains 3 folders with 1951 train images, 106 test images and 253 validation images. Each folder is divided into four classes: diseased cotton plant (Fusarium Wilt), diseased cotton leaf (Leaf Curl Disease), fresh cotton plant (Healthy Plant) and fresh cotton leaf (Healthy Leaf). Each image has a size of 694x694 pixels in JPG format.
Here are the sample images of the dataset...  

<img src="" width=50% height=50%>

## Training Accuracy and Loss
<img src="">

## Confusion Matrix
<img src="" width=50% height=50%>

## Tech Stack Used
1. Python 
2. Flask
3. Deep Learning (CNN Architecture)
4. Docker

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

## Project Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. app.py

## Deployment Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536973-4530fe7d-5509-4609-bfd2-cd702fc82423.png)


### Step 1: Clone the repository
```bash
git clone https://github.com/shubhkirti123/cotton-disease-classification-project
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n cotton python=3.8 -y
```

```bash
conda activate cotton
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

## AWS-CICD-Deployment-with-Github-Actions

### 1. Login to AWS console.

### 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
### 4. Create EC2 machine (Ubuntu) 

### 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
## 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


## 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app