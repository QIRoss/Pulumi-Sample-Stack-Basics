"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

bucket = s3.BucketV2('my-bucket')

pulumi.export('bucket_name', bucket.id)
