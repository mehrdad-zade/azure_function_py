import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    csv_data = """
    id,name,age,city,country
    1,John,25,New York,USA
    2,Alice,28,Paris,France
    3,Bob,22,London,UK
    4,Eve,30,Berlin,Germany
    5,Charlie,27,Tokyo,Japan
    """

    headers = {
        "Content-type": "text/plain",
        "Content-Disposition": "inline; filename=sample_data.csv"
    }

    return func.HttpResponse(csv_data, headers=headers)