import boto3
from botocore.exceptions import ClientError
import time
import uuid



class todoTable(object):
    def __init__(self, table, dynamodb=None):
        self.tableName = table
        if not dynamodb:
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url="http://172.18.0.1:8000")
        self.dynamodb = dynamodb
   
    def create_todo_table(self):
        table = self.dynamodb.create_table(
            TableName=self.tableName,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        

        # Wait until the table exists.
        table.meta.client.get_waiter(
            'table_exists').wait(TableName=self.tableName)
        if (table.table_status != 'ACTIVE'):
            raise AssertionError()

        return table

    def delete_todo_table(self):
        table = self.dynamodb.Table(self.tableName)
        table.delete()

    def put_todo(self, text):
# A completar por el alumno. Pista: todos/ToDoPutItem.py """
        
        try:
        
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url="http://172.18.0.1:8000")
            self.dynamodb=dynamodb
            
            table= self.dynamodb.Table(self.tableName)
          
            timestamp = str(time.time())
        
            item={
                    'id': str(uuid.uuid1()),
                    'text': text,
                    'checked': False,
                    'createdAt': timestamp,
                    'updatedAt': timestamp,
             }
            table.put_item(Item=item)
                
               
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return item
    
           


    def get_todo(self, id):
 # A completar por el alumno. Pista: todos/ToDoGetItem.py """
        try:
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url="http://172.18.0.1:8000")
            self.dynamodb=dynamodb
            table = self.dynamodb.Table(self.tableName)
    
        
            response = table.get_item(
                Key={
                    'id': id
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response

    def scan_todo(self):
# A completar por el alumno. Pista: todos/ToDoListItems.py """
        try:
            self.dynamodb = boto3.resource(
                'dynamodb', endpoint_url= "http://172.18.0.1:8000")
            
       
            table = self.dynamodb.Table(self.tableName)
            # fetch all todos from the database
            response = table.scan()
    
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response

    def update_todo(self, text, id, checked):
# A completar por el alumno. Pista: todos/ToDoUpdateItem.py """
        
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url="http://172.18.0.1:8000")
            self.dynamodb=dynamodb
            table = self.dynamodb.Table(self.tableName)
            
            timestamp = str(time.time())
            try:    
                response = table.update_item(
                    Key={
                        'id': id
                    },
                    ExpressionAttributeNames={
                        '#todo_text': 'text',
                    },
                    ExpressionAttributeValues={
                        ':text': text,
                        ':checked': checked,
                        ':updatedAt': timestamp,
                    },
                    UpdateExpression='SET #todo_text = :text, '
                                     'checked = :checked, '
                                     'updatedAt = :updatedAt',
                    ReturnValues='ALL_NEW',
                )
            except ClientError as e:
                print(e.response['Error']['Message'])
            else:
                return response

    def delete_todo(self, id):
#  A completar por el alumno. Pista: todos/ToDoDeleteItem.py """
        try:
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url="http://172.18.0.1:8000")
            self.dynamodb=dynamodb
            table = self.dynamodb.Table(self.tableName)
    
        
            # delete the todo from the database
            response = table.delete_item(
                Key={
                    'id': id
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response
            
    