#!/bin/bash
set -e
#get authentication
bearer_id=$(curl -H "Content-Type: application/json" -X POST --data @"cloud_auth.json" https://xray.cloud.xpand-it.com/api/v1/authenticate)
in_token=${bearer_id}
#strip not needed characters
out_token=`echo ${in_token} | sed 's/.\(.*\)/\1/' | sed 's/\(.*\)./\1/'`
#usage example
echo $out_token
