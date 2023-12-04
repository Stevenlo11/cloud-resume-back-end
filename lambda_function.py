import json
import boto3

def lambda_handler(event, context):
    
    # Connect to our DynamoDB resource
    client = boto3.resource('dynamodb')
    
    # Create a Dynamodb client for the visitor_count table
    table = client.Table('visitor_count')
    
    
    # Increment visitor_count for index.html
    response = table.update_item(
        Key={
            'path': 'index.html'
        },
        AttributeUpdates={
            'visitor_count': {
                'Value': 1,
                'Action': 'ADD'
            }
        }
    )
    
    
    # Get visitor_count from the visitor_count table for indexhtml
    response = table.get_item(
        Key={
            'path':'index.html'
        }
    )
    visitor_count = response['Item']['visitor_count']
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body':visitor_count
    }