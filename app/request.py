import urllib.request,json
from .models import Quote

#Getting the base url
base_url = None

def configure_request(app):
    global base_url
    base_url= app.config["QUOTE_API_BASE_URL"]

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

    return get_quotes_response
    #     quote_results = None
    #     if get_quotes_response:

    #         quote_results_list = get_quotes_response
    #         quote_results = process_results(quote_results_list)

    # return get_quotes_response

# def process_results(quote_list):
#     '''
#     Function  that processes the quote result and transform them to a list of Objects
#     Args:
#         quote_list: A list of dictionaries that contain quote details
#     Returns :
#         quote_results: A list of movie objects
#     '''
#     quote_results = []
#     for quote_item in quote_list:
#         id = quote_item.get('id')
#         quote = quote_item.get('original_title')
#         author = quote_item.get('overview')
#         quote_object = Quote(id,author,quote)
#         quote_results.append(quote_object)

#     return quote_results