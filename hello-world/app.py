"""Lambda function to be used in the API Gateway Tutorial Lab-01"""

from typing import Any, Dict, Iterable, List, Optional
import os
import json
import logging
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.event_handler.api_gateway import (
    APIGatewayRestResolver,
    Response,
)
from http import HTTPStatus
from aws_lambda_powertools.logging import correlation_paths
from log_formatter import CustomFormatter

logger = Logger(
    service="serverless-lab-01",
    sample_rate_value=0.1,
    logger_formatter=CustomFormatter(),
)
tracer = Tracer(service="apigw-lab-01")
app = APIGatewayRestResolver()


@app.get("/hello")
def get_hello():
    """
    Process the GET /hello endpoint
    """

    query_string_parameters = app.current_event.query_string_parameters or {}
    greeter = query_string_parameters.get("greeter", None)
    message = {
        "message": f"Hello, {greeter} !",
        "httpMethod": "GET",
        "source": "queryStringParameters",
    }

    ## If the greeter is not found in query string parameter then check
    ## multi value query string parameters
    if not greeter:
        logger.info(
            "Greeter not found in query string parameter! checking multi value query string parameters"
        )
        multi_value_query_string_parameters = (
            app.current_event.multi_value_query_string_parameters or {}
        )
        greeter = multi_value_query_string_parameters.get("greeter", [None])[0]
        message = {
            "message": f"Hello, {greeter} !",
            "httpMethod": "GET",
            "source": "multiValueQueryStringParameters",
        }

    ## If the greeter is not found in multi value query string parameterw then check
    ## request headers
    if not greeter:
        logger.info(
            "Greeter not found in multi value query string parameters! checking headers"
        )
        headers = app.current_event.headers
        greeter = headers.get("greeter", None)
        message = {
            "message": f"Hello, {greeter} !" if greeter else "Hello, Guest!",
            "httpMethod": "GET",
            "source": "headers",
        }

    if not greeter:
        return Response(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content_type="application/json",
            body=json.dumps(message),
        )
    return Response(
        status_code=HTTPStatus.OK,
        content_type="application/json",
        body=json.dumps(message),
    )


@app.post("/hello")
def post_hello():
    """
    Process the POST /hello endpoint
    """
    logger.info("POST /hello")

    try:
        request_body = app.current_event.json_body
    except json.JSONDecodeError:
        logger.error("Invalid JSON in request body")
        return Response(
            status_code=HTTPStatus.BAD_REQUEST,
            content_type="application/json",
            body=json.dumps({"message": "Invalid JSON format"}),
        )

    greeter = request_body.get("greeter", None)
    message = {"message": f"Hello, {greeter} !", "httpMethod": "POST", "source": "body"}

    if not greeter:
        return Response(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content_type="application/json",
            body=json.dumps({"message": "Internal Server Error", "httpMethod": "POST"}),
        )
    return Response(
        status_code=HTTPStatus.OK,
        content_type="application/json",
        body=json.dumps(message),
    )


@logger.inject_lambda_context(
    correlation_id_path=correlation_paths.API_GATEWAY_REST, log_event=True
)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    """
    AWS Lambda function handler
    """
    return app.resolve(event, context)
