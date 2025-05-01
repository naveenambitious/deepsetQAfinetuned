# deepsetQAfinetuned
This model is fine tuned on SqaudV2 dataset and it is on base model deepset QA.

This project contains Docker file and requirements. The user is requested to setup docker container as per the requirement file. 
The app folder contains following files:
db_utils.py  
main.py  
model.py  
roberta_pubmed_qa_modelV1.1  
talk_model.py  

The model.py file is helpful to load the fine tuned model. The main.py file is the only start point to take the user input {question, context}, and send it to the tal_model.py.
The roberta_pubmed_qa_modelV1.1 is the directory that keeps the fine tuned model.

Note; due to size limitation, model.safetensors can be provided on request.


Request on: navi9999@gmail.com
