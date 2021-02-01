import os
import todoTable 
import boto3



def delete(event, context):
    
  
    # delete the todo from the database
    table = todoTable.todoTable("todoTable")
    table.delete_todo( id = event['pathParameters']['id'])
       

    # create a response
    response = {
        "statusCode": 200
    }

    return response
