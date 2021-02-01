import json
import logging
import os
import time
import uuid
import todoTable
import boto3
from botocore.exceptions import ClientError


def create(event, context):
    
    table = todoTable.todoTable("todoTable")
    data = json.loads(event['body'])
    
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
        return
        
    # write the todo to the database
    item = table.put_todo(text=data['text'])
        
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    
    return response   
   
