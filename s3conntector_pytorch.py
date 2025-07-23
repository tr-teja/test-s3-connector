import s3torchconnector

import boto3
import botocore
import io
import itertools
from PIL import Image
import torch
import torchdata
import torchvision
import webdataset

IMAGES_URI = "s3://tractable-images-narwhal-anonymised/"
# SHARDS_URI = "s3://s3torchconnector-demo/geonet/shards/"
# CHECKPOINT_URI = "s3://s3torchconnector-demo/checkpoint/"
REGION = "us-east-1"



dataset = s3torchconnector.S3IterableDataset.from_prefix(IMAGES_URI, region=REGION)#, s3client_config=config)

