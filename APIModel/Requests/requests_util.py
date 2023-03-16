
# Tool used to handle requests

# validate to check if a request is valid or not
# for example, if the request has a blank field that is not supposed to be blank,
# then the program should throw an error or raise exception.
def validate_request(request_param):
    if (request_param[0] == "Valid"):
        return "This is a valid request, continue with program execution"
    else:
        return "This is not a valid request, throw an error"

# retrieve key details from the request that is sent to the server.
def retrieve_request_info(request_param):
    customer_id = request_param[0]
    customer_tools = request_param[1]
    return [customer_id, customer_tools]
    