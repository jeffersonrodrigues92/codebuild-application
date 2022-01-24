
import logging

from service.sns_service import SNSService
from repository.account_repository import AccountRepository

class AccountService:

    sns_service = SNSService()
    account_repository = AccountRepository()

    def validate_account(self, event_response):

        try:
            
            account_response =  self.account_repository.find_account_by_id(event_response['account'])

            if account_response['status']:
                logging.warn("account is active")
                self.sns_service.publish(event_response)
            else:
                logging.info(f"account not actived {event_response['account']}")
                raise Exception("account not found")
                
        except Exception as exception:
            raise exception
