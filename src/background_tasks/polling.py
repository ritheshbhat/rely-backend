import csv
import time
# poll for any changes in dataset, and update the database.

import urllib.request
import os

import boto3
import pandas as pd
from werkzeug.exceptions import abort

from src.rely.utils.configs import AppConfig, log


class FileManager:
    def __init__(self, file_name, ac: AppConfig):
        self.file_name = file_name
        self.ac = ac
        if ac.s3_endpoint is None:
            self.s3 = boto3.client('s3',
                                   region_name=ac.s3_region,
                                   aws_access_key_id=ac.aws_access_key,
                                   aws_secret_access_key=ac.aws_secret_key)
        else:
            self.s3 = boto3.client('s3',
                                   endpoint_url=ac.s3_endpoint,
                                   region_name=ac.s3_region,
                                   aws_access_key_id=ac.aws_access_key,
                                   aws_secret_access_key=ac.aws_secret_key)

        self.local_file_path = os.path.join(ac.tmp_loc, file_name)

    def download_dataset_and_insert(self):
        try:
            url = self.ac.dataset_url
            filename = os.path.join(self.ac.tmp_loc, "dataset.csv")

            urllib.request.urlretrieve(url, filename)
            log.debug("downloading-file-from-bucket...")
        except Exception as e:
            log.info("err-while-downloading")

            # abort(500, f"err-while-downloading-from-bucket => ${e}")

    def delete_local_dataset_file(self):
        try:
            log.debug(f"deleting file {self.local_file_path}")
            os.remove(self.local_file_path)
        except Exception as e:
            abort(500, f"err-while-deleting-file => ${e}")

    def upload_file_to_s3_bucket(self, file_name, bucket_name):
        try:
            log.debug(f"uploading {file_name} file to s3...")
            self.s3.upload_file(os.path.join(self.ac.tmp_loc, file_name), bucket_name,
                                file_name)
            log.debug(f"{file_name} upload successful")
        except Exception as e:
            abort(500, f"err-while-uploading-parsed-output {e}")


def start_polling(app):
    pass
    # while True:
    #     log.info("polling for new dataset.")
    #     ac = AppConfig(app)
    #     fm = FileManager(ac.dataset, ac)
    #     fm.download_dataset_and_insert()
    #     ad = []
    #     #load dataset in redis
    #     with open('dataset.csv', 'r') as csvfile:
    #         csv_reader = csv.DictReader(csvfile)
    #         for row in csv_reader:
    #             # Get the key from the desired column
    #             key = row['CITY']
    #             price = row['PRICE']
    #             add = row['ADDRESS']
    #             ad.append(add)
    #             url = row['URL']
    #             if price == "" or type(price)!=str:
    #                 price = 0
    #             key = key.replace(" ","").lower()
    #             # Convert the row data to a list of key-value pairs
    #             row_data = ["address:"+add,"price:"+price,"url:"+url]
    #             ac.redis.rpush(key, *row_data)
    #     print("all the address are")
    #     print(ad)
    #     log.info("sleeping for 15 minutes")
    #     time.sleep(900)
