sam build
sam package --s3-bucket mybucket --output-template-file packaged.yaml
sam deploy --template-file packaged.yaml --stack-name mystack --capabilities CAPABILITY_IAM
