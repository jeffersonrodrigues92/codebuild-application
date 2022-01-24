import boto3

from boto3.dynamodb.conditions import Attr, Key

class AccountRepository:

    def find_account_by_id(self, account_id):
        
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
        table = dynamodb.Table('account')

        try:
        
            response = table.get_item(Key={'id' : account_id})

            if 'Item' in response:
                return response['Item']
            else:
                raise Exception(f'account_id not found {account_id}')

        except Exception as exception:
            raise exception
