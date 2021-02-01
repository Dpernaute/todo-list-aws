import json
import os
import todoTable 
import decimalencoder
import boto3



def list (event, context):
    
    table = todoTable.todoTable("todoTable")
    # fetch all todos from the database
    result = table.scan_todo()
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
