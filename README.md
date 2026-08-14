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


======XXXXXXXXXXXXXXXXXXXXX======================
pubmedqa_to_squad.ipynb notebook converts preprocessed PubMedQA data into the SQuAD v2.0 JSON format used by standard question-answering pipelines. It reads the flattened PubMedQA records from combined_output.csv, then for each question it pairs the contexts field with the long_answer field and attempts to locate the answer text as an exact substring within the context using string matching. Where a match is found, the question is recorded as answerable with the matched character offset (answer_start); where no exact match is found, the question is marked is_impossible: true, following the SQuAD v2.0 convention for unanswerable questions rather than being dropped or given an incorrect span.
Input file: combined_output.csv  original PubMedQA dataset, produced from pubmedqa.ipynb
Output file: data.json — a SQuAD v2.0-format JSON file containing one paragraph/question-answer set per PubMedQA record, structured as {"version": "v2.0", "data": [{"title", "paragraphs": [{"context", "qas": [{"id", "question", "answers", "is_impossible"}]}]}]}. This file can be used directly as input to any SQuAD-format QA training. [file size limit (125 Mb file size)]

Note: due to size limitation, model.safetensors can be provided on request.


Request on: navi9999@gmail.com
