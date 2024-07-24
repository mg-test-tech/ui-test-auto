import re
import requests
from variables import *


def get_token_value_by_regex(regex_pattern, input):
    """
    We need to extract csrf token values and pass it with next request, also
    we need to extract auth token values from responses for both, implicit
    and client/secret cases
    regex_pattern: str, regex pattern to extract values, in variables file
    input: str, pass string from where value needs to be extracted
    return:
    """
    find_token_body = re.search(regex_pattern, str(input))
    # print(find_token_body)
    captured_token = find_token_body.group(1)
    return captured_token


def get_token_implicit(name, pwd):
    """
    This function is to get implicit based authentication.
    See comments in function.
    request.Session used to handle cookies, and the same session needs to be
    used through the flow to keep it going
    param name: str, username
    param pwd: str, password
    return: str, bearer token
    """
    session = requests.Session()
    # --------------------------------------------------------------------
    # send the request, capture csrf token
    login_1 = session.get(accounts_host + login_path)
    print(login_1.url)
    print(login_1.status_code)
    login_1_body = login_1.text
    csrf_login_1 = get_token_value_by_regex(regex_pattern=csrf_body_pattern,
                                            input=login_1_body)
    # --------------------------------------------------------------------
    # send request to login, pass csrf token
    login_2_headers = {'Referer': accounts_host + login_path + '?next=/'}
    login_2_data = {'csrfmiddlewaretoken': csrf_login_1,
                    'username': name,
                    'password': pwd,
                    'next': '/'}
    session.post(accounts_host + login_path, headers=login_2_headers,
                 data=login_2_data)
    # --------------------------------------------------------------------
    # send request, capture bearer token. The request needs to be URL encoded
    # and parameter allow_redirect set to False
    auth_1_headers = {'Referer': accounts_host + login_path + '?next=/',
                      'Connection': 'keep-alive',
                      'Accept': 'application/json'}
    auth_1 = session.get(
        accounts_host + auth_path + '?redirect_uri=https%3A%2F%2F' +
        api_url + '%2Fui%2Foauth2-redirect.html&client_id=swagger_client&response_type=token',
        headers=auth_1_headers, allow_redirects=False)
    # print(auth_1.headers)
    # print(auth_1.text)
    header_data = auth_1.headers['Location']
    bearer_regex_pattern = '#access_token=(.+?)&expires_in'
    bearer_token = get_token_value_by_regex(regex_pattern=bearer_regex_pattern,
                                            input=header_data)
    # --------------------------------------------------------------------
    return bearer_token


def get_all_tokens(name, pwd):
    '''
    This function is to get client/secret based authentication.
    See comments in function.
    request.Session used to handle cookies, and the same session needs to be
    used through the flow to keep it going
    param name: str, username
    param pwd: str, password
    return: user, secret, basic_token, bearer_token
    '''
    session = requests.Session()
    # ------------------------------------------------------------------------
    # send the request, capture csrf
    acc_response = session.get(accounts_host + start_path)
    acc_response_body = acc_response.text
    csrf_token_body = get_token_value_by_regex(regex_pattern,
                                               input=acc_response_body)
    # ------------------------------------------------------------------------
    # login with valid credentials, pass csrf with request
    login_headers = {'referer': accounts_host + start_path}
    login_data = {'csrfmiddlewaretoken': csrf_token_body,
                  'username': name,
                  'password': pwd,
                  'next': api_cred_path}
    # print(login_data)
    session.post(accounts_host + login_path, headers=login_headers,
                 data=login_data)
    session.get(accounts_host + api_cred_path)
    # -----------------------------------------------------------------------
    # send the request, capture csrf
    api_response = session.get(accounts_host + api_cred_path)
    api_response_body = api_response.text
    # print(api_response_body)
    csrf_token_api = get_token_value_by_regex(regex_pattern,
                                              input=api_response_body)
    # print(csrf_token_api)
    # ------------------------------------------------------------------------
    # send request, pass csrf with request, capture user, secret, and basic
    # tokens
    token_headers = {'X-csrftoken': csrf_token_api,
                     'Referer': accounts_host + api_cred_path,
                     'X-requested-with': 'XMLHttpRequest',
                     'Accept': '*/*'}
    token_data = {"key_name": "qa_api_key"}
    token_response = session.post(accounts_host + api_cred_path,
                                  headers=token_headers, json=token_data)
    tokens = token_response.text
    # print(tokens)
    user = get_token_value_by_regex(regex_user, input=tokens)
    secret = get_token_value_by_regex(regex_secret, input=tokens)
    basic_token = get_token_value_by_regex(regex_token, input=tokens)
    # -----------------------------------------------------------------------
    # send request with basic token and capture bearer token
    bearer_headers = {'Authorization': 'Basic ' + basic_token}
    bearer_data = {"grant_type": "client_credentials"}
    bearer_response = session.post(auth_host + bearer_path,
                                   headers=bearer_headers,
                                   json=bearer_data)
    print(bearer_response.url)
    full_bearer_response = bearer_response.text
    print(full_bearer_response)
    bearer_token = get_token_value_by_regex(regex_bearer,
                                            input=full_bearer_response)
    # -----------------------------------------------------------------------
    return user, secret, basic_token, bearer_token
