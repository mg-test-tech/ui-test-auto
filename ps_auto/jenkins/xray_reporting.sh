#!/bin/bash
set -e

curl -H "Content-Type: application/json" -X POST --data @"cloud_auth.json" https://xray.cloud.xpand-it.com/api/v1/authenticate

bearer_id=$(curl -H "Content-Type: application/json" -X POST --data @"cloud_auth.json" https://xray.cloud.xpand-it.com/api/v1/authenticate)

in_token=${bearer_id}
out_token=`echo ${in_token} | sed 's/.\(.*\)/\1/' | sed 's/\(.*\)./\1/'`

new_issue=$(curl -H "Content-Type: application/json" -X POST -H "Accept: application/json" --user development@test.com:password --data @"new_issue.json" "https://test.atlassian.net/rest/api/2/issue/") 
# echo '------------------------------------------------------------------------------------'
# echo ${new_issue}
# echo '------------------------------------------------------------------------------------'
in_number=`echo ${new_issue} | jq '."key"'`
issue_number=`echo ${in_number} | sed 's/.\(.*\)/\1/' | sed 's/\(.*\)./\1/'`

#f running against execution, new ticket is created, then test execution updated. need to have empty execution
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_1.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_2.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_3.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_4.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}

curl -D- --user development@test.com:password -X POST --data @issue_update.json -H "Content-Type: application/json" "https://test.atlassian.net/rest/api/2/issue/${issue_number}/transitions?expand=transitions.fields"
# timestamp() {
#   date +"%T"
# }


# id: "211"

#!/bin/bash
set -e
#get authentication
bearer_id=$(curl -H "Content-Type: application/json" -X POST --data @"cloud_auth.json" https://xray.cloud.xpand-it.com/api/v1/authenticate)
in_token=${bearer_id}
#strip not needed characters
out_token=`echo ${in_token} | sed 's/.\(.*\)/\1/' | sed 's/\(.*\)./\1/'`
#usage example
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Company_Reports.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
