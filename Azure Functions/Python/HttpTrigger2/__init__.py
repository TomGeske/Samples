import logging

import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    from sqlalchemy import Column, Integer, String
    from sqlalchemy import create_engine

    engine = create_engine('sqlite:///sales.db', echo = True)

    response = req.params.get('response')
    if not response:
        try:
            response = requests.get("https://github.com/timeline.json")
        except ValueError:
            pass
        else:
            responseContent = response.json() 

    if responseContent:
        return func.HttpResponse(f"API Result: {responseContent}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
