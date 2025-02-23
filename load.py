import boto3

#Define AWS details 
local_file = 'transformed_weather_data.csv'
bucket_name = 'open-weather-api-data'
s3_file_name = 'weather_data/transformed_weather_data.csv'

#Start the S3 Client 
s3 = boto3.client('s3')

#Function that loads data to s3 

def upload_to_s3(local_file,bucket_name,s3_file_name):
    try:
        s3.upload_file(local_file, bucket_name, s3_file_name)

        print(f"File '{local_file}' uploaded to S3 bucket '{bucket_name}' as '{s3_file_name}'") 

    except Exception as e:

        print(f"Error uploading file: {e}") 

upload_to_s3(local_file, bucket_name, s3_file_name) 
