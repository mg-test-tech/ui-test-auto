#!/bin/bash
set -e

Message_bad='"The test is FAIL. Result - FAILURE. The link to the Allure Report is: '${BUILD_URL}'allure"'
Password=${JIRA_PWD}
id=${client_id}
secret=${client_secret}

echo "-----------------Start reporting to Jira---------------------------------------------------------"
curl -D- -u development@test.com:${Password} -X PUT --data '{"update": {"customfield_15162": [{"set": {"id":"22228"}}]}}' -H "Content-Type: application/json" https://test.atlassian.net/rest/api/2/issue/${RELEASE_TICKET};
curl -D- -u development@test.com:${Password} -X PUT --data '{"update": {"customfield_15163": [{"set": '"${Message_bad}"'}]}}' -H "Content-Type: application/json" https://test.atlassian.net/rest/api/2/issue/${RELEASE_TICKET};
curl -D- -u development@test.com:${Password} -X POST --data '{"body": '"${Message_bad}"'}' -H "Content-Type: application/json" https://test.atlassian.net/rest/api/2/issue/${RELEASE_TICKET}/comment;
echo "-----------------Ends reporting to Jira---------------------------------------------------------"

echo "-----------------Start reporting to XRay------------------------------------------------------"
bearer_id=$(curl -H "Content-Type: application/json" -X POST --data '{"client_id": '"${id}"',"client_secret": '"${secret}"'}' "https://xray.cloud.xpand-it.com/api/v1/authenticate")

in_token=${bearer_id}
out_token=`echo ${in_token} | sed 's/.\(.*\)/\1/' | sed 's/\(.*\)./\1/'`

# create new test execution issue and remove commas
new_issue=$(curl -H "Content-Type: application/json" -H "Accept: application/json" -X POST -u development@test.com:${Password} --data '{"fields": {"project": {"key": "QS"},"summary":"SANITY TEST EXECUTION FOR BUILD '${BUILD_NUMBER}', RELEASE TICKET '${RELEASE_TICKET}'","issuetype": {"id": "11826"},"description": "EXECUTION RESULTS: '${BUILD_URL}'allure"}}' "https://test.atlassian.net/rest/api/2/issue/") 

in_number=`echo ${new_issue} | jq '."key"'`
issue_number=`echo ${in_number} | sed 's/.\(.*\)/\1/' | sed 's/\(.*\)./\1/'`

# import test results to the new test execution
cd ./src/qa_testing/bdd/sanity_01/junit_reports

curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Comparisson_Report.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Confidential_Company.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Data_Entry.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Healthmark.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Login_Logout.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Matrix_Report.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-SSO_Login_Logout.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}
curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${out_token}"  --data @"TESTS-Company_Reports.xml" https://xray.cloud.xpand-it.com/api/v1/import/execution/junit?testExecKey=${issue_number}

# change status to new test execution to Done
curl -H "Content-Type: application/json" -X POST --user development@test.com:${Password} --data '{"transition": {"id": "211"}}' https://test.atlassian.net/rest/api/2/issue/${issue_number}/transitions?expand=transitions.fields

echo "-----------------Ends reporting to XRay------------------------------------------------------"

#remove result xml files
cd ..
rm ./junit_reports/*

# {"transition": {"id": "41"}}
# {"transition": {"id": "211"}}
