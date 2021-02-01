import os
import json
import todoTable
import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    
    
    # fetch todo from the database
    table = todoTable.todoTable("todoTable")
    result = table.get_todo(id = event['pathParameters']['id'])
       

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
