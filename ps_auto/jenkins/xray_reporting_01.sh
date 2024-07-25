#!/bin/bash
set -e

Password="password"
RELEASE_TICKET="RRD-0001"
client_id="client_id"
client_secret="client_secret"
BUILD_URL="https://jenkins.ci.tests.co/view/Work%20In%20Progress/job/XRAY_REPORTING_TRY_00/37/"
BUILD_NUMBER="2201"

bearer_id=$(curl -H "Content-Type: application/json" -X POST --data '{"client_id": "'${client_id}'","client_secret": "'${client_secret}'"}' "https://xray.cloud.xpand-it.com/api/v1/authenticate")
in_token=${bearer_id}
out_token=`echo ${in_token} | sed 's/.\(.*\)/\1/' | sed 's/\(.*\)./\1/'`
echo ${bearer_id}
new_issue=$(curl -H "Content-Type: application/json" -H "Accept: application/json" -X POST --user development@test.com:${Password} --data '{"fields": {"project": {"key":"RRQ"},"summary":"SANITY TEST EXECUTION FOR BUILD '${BUILD_NUMBER}', RELEASE TICKET '${RELEASE_TICKET}'","issuetype": {"id": "11826"},"description": "EXECUTION RESULTS: '${BUILD_URL}'allure","components": [{"id": "13546"}]}}' "https://test.atlassian.net/rest/api/2/issue/") 
echo ${new_issue}
in_number=`echo ${new_issue} | jq '."key"'`
issue_number=`echo ${in_number} | sed 's/.\(.*\)/\1/' | sed 's/\(.*\)./\1/'`
curl -D- -u development@test.com:${Password} -X PUT --data '{"accountId": "557058:d04e15d7-f74d-412d-b8cb-8c012056f4a8"}' -H "Content-Type:application/json" 'https://test.atlassian.net/rest/api/2/issue/'${issue_number}'/assignee'

cd ./junit_reports
response=$(curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_1.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number})
echo ${response}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_1.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_2.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_3.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_4.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_5.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_6.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_7.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Test_8.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}

curl -H "Content-Type: application/json" -X POST --user development@test.com:${Password} --data '{"transition": {"id": "41"}}' https://test.atlassian.net/rest/api/2/issue/${issue_number}/transitions?expand=transitions.fields

