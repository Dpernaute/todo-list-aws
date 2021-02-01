import json
import time
import logging
import os
import todoTable 
import decimalencoder
import boto3



def update(event, context):
    data = json.loads(event['body'])
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return

    

    # update the todo in the database
    table = todoTable.todoTable("todoTable")
    result = table.update_todo(text = data['text'],id = event['pathParameters']['id'],checked = data['checked'])
       

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
