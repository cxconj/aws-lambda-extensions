# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import os
from pathlib import Path
from datetime import datetime
from random import randint

def lambda_handler(event, context):
	print(json.dumps({"company_id":randint(0,100), "created_at":str(datetime.now())}))
	return {
		'statusCode': 200,
		'body': json.dumps('Hello from Lambda!')
	}
