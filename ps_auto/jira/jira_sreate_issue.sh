#!/bin/bash
set -e

# response=$(curl -H "Content-Type: application/json" -X POST -H "Accept: application/json" --user development@test.com:password --data @"new_issue.json" "https://test.atlassian.net/rest/api/2/issue/") 


# echo '{"id":"213570","key":"QS-196","self":"https://test.atlassian.net/rest/api/2/issue/213570"}' | jq '."key"'


# echo '{"id":"213570","key":"QS-196","self":"https://test.atlassian.net/rest/api/2/issue/213570"}' | jq '."key"' > ./out_value_file.txt
in_number=`echo '{"id":"213570","key":"QS-196","self":"https://test.atlassian.net/rest/api/2/issue/213570"}' | jq '."key"'`

issue_number=`echo ${in_number} | sed 's/.\(.*\)/\1/' | sed 's/\(.*\)./\1/'`


echo ${issue_number}
