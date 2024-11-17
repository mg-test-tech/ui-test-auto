def navigate_to_url(context, URL):
    '''
    Description: navigate to given URL
    :param context: context
    :param URL: str, URL to navigate to
    '''
    context.browser.get(URL)

