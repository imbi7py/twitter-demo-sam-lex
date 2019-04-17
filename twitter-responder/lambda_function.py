import os
import boto3
import twitter

ssm = boto3.client("ssm")
lex = boto3.client("lex-runtime")
SSM_CREDS_NAME = os.getenv("SSM_CREDS_NAME")
CREDS = ssm.get_parameter(Name=SSM_CREDS_NAME)['Parameter']['Value'].split(',')
twitter_api = twitter.Api(*CREDS)


# lambda is invoked by APIGW via direct message twitter webhook
def lambda_handler(event, context):
#    resp = lex.post_text(
#       botName="botname",
#       botAlias="$LATEST", # use prod in prod
#       userId=event['DirectMessage']['screen_name'],
#       sessionAttributes={},
#       inputText=event['DirectMessage'][0]['text'])
#    twitter_api.PostDirectMessage(user, resp['Intent']['text'])
     return "hello, world"
