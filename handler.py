from service.account_service import AccountService
from service.file_service import FileService

account_service = AccountService()
file_service = FileService()

def lambda_handler(event, context):

    event_response = file_service.get_object(event['Records'][0]['s3']['object']['key'])
    account_service.validate_account(event_response)

if __name__ == '__main__':
    event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2021-07-09T00:29:18.445Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDA4MNAYIIDRV4UU7OKB'}, 'requestParameters': {'sourceIPAddress': '177.68.240.217'}, 'responseElements': {'x-amz-request-id': 'CHQJPXD09MPCT4SY', 'x-amz-id-2': 'C1r1/2KRiFqz+c2hVQ5/3noYbVqMcvMHcyCMBysAsj26ZzVSN8Ae08PzM1VPLijrj9Nfzhk0hwU40u0bqIpUHxdv8ElCoJ0feExN76zspoU='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'taura-events', 'bucket': {'name': 'taura-events', 'ownerIdentity': {'principalId': 'A3NEUTLVG54SZG'}, 'arn': 'arn:aws:s3:::taura-events'}, 'object': {'key': 'AuthorizeSecurityGroupIngress_945224557198_2021-07-08T00_02_35Z', 'size': 1701, 'eTag': 'be9a51511e65730b9f9c57a6de3a0c59', 'sequencer': '0060E7985E97B17C1D'}}}]}

    lambda_handler(event, None)



