#!/usr/bin/bash
# Report build status to Jira Ticket
set -e
set -x

env

BUILD_RESULT=${BUILD_RESULT:-UNKNOWN}
TEST_SUITE=${TEST_SUITE:-sanity}
TEST_NAME="${NAMESPACE} ${TEST_SUITE}"

PREF="${TEST_NAME^} result - ${BUILD_RESULT}."
ALLURE_LINK="${BUILD_URL}allure/"

declare -A STATUS_MAP=(
    [SUCCESS]="${PREF}\nThe link to the Allure Report is: ${ALLURE_LINK}"
    [UNSTABLE]="${PREF}\nSome behave tests failed. \nPlease check allure report ${ALLURE_LINK}"
    [FAILURE]="Pipeline is broken ${BUILD_URL}"
    [NOT_BUILT]="${PREF} ${ALLURE_LINK}"
    [ABORTED]="${PREF} ${ALLURE_LINK}"
    [UNKNOWN]="${PREF} ${ALLURE_LINK}"
)

# RRI Test Result
declare -A JIRA_STATUS_MAP=(
    [SUCCESS]=22227  # Passed
    [UNSTABLE]=22228  # Failed
    [FAILURE]=22228  # Failed
    [NOT_BUILT]=""
    [ABORTED]=""
    [UNKNOWN]=""
)

RESOLUTION=${STATUS_MAP[$BUILD_RESULT]}
RESOLUTION=${RESOLUTION:-""}

JIRA_TICKET=${JIRA_TICKET:-$RELEASE_TICKET}
# Get jira ticket from environment variables
# TICKET -> JIRA_TICKET -> RELEASE_TICKET
TICKET=${TICKET:-$JIRA_TICKET}

[[ -z $TICKET ]] && (
    echo 'No ticket to report to'
    exit 0
)

JIRA_API2=https://test.atlassian.net/rest/api/2

function jira_curl() {
    curl --dump-header - \
        -u "${JIRA_USR}:${JIRA_PWD}" \
        -H "Content-Type: application/json" "$@" \
        ;
}

if [[ -n $RESOLUTION ]]; then
    cat << JSON | jq '.' | jira_curl --data @- "$JIRA_API2/issue/$TICKET/comment"
{"body": "$RESOLUTION"}
JSON

    RRI_TEST_RESULT=${JIRA_STATUS_MAP[$BUILD_RESULT]}
    # Set RRI Test Result field for Jira Ticket
    cat << JSON | jq '.' | jira_curl -X PUT --data @- "$JIRA_API2/issue/$TICKET"
{
  "update": {
    "customfield_15162": [{"set": {"id": "${RRI_TEST_RESULT}"}}],
    "customfield_15163": [{"set": "$RESOLUTION"}]
  }
}
JSON
fi
