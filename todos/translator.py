import os
import json
import time
import logging
import todoTable 
import decimalencoder
import boto3
import get




def translator(event, context):
    
    translate = boto3.client('translate')
    
    # fetch todo from the database
    table = todoTable.todoTable("todoTable")
    response= table.get_todo(id =event['pathParameters']['id'])
    
        
    #extract text from response and translate      
    result = {
        
        'text' : translate.translate_text(Text = response['Item']['text'], 
            SourceLanguageCode ='auto', TargetLanguageCode = event['pathParameters']['language'])
        
    }
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['text']['TranslatedText'],
        cls=decimalencoder.DecimalEncoder)
    }

    return response