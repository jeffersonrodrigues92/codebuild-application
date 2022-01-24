import boto3
import ast

class FileService:

    def get_object(self, key):
        
        s3 = boto3.client('s3', region_name="us-east-1")

        try:

            response = s3.get_object(Bucket='taura-events', Key=key)
            return ast.literal_eval(response['Body'].read().decode('utf-8').replace("\'", "\""))
            
        except Exception as exception:
            raise exception