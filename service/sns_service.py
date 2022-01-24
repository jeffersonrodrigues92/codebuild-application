import logging
import boto3

class SNSService:

    def publish(self, event):
        
        sns = boto3.client('sns', region_name="us-east-1")

        try:
    

            logging.info("creating event to publish")

            response = sns.publish(
                TopicArn='arn:aws:sns:us-east-1:851277529607:taura-events-security',
                Message= str(event),
                MessageAttributes={
                'origin': {
                    'DataType': 'String',
                    'StringValue': event['detail']['eventSource']
                }
            })

            logging.info("event published")

        except Exception as exception:
            raise exception
