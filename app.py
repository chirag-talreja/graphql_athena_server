from api import app, athena_connection
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import HTTP_STATUS_200_OK
from flask import request, jsonify
from ariadne import ScalarType
from Constants import PLAYGROUND_HTML
from api.queries import listBackups_resolver,getBackup_resolver

datetime_scalar = ScalarType("Datetime")

@datetime_scalar.serializer
def serialize_datetime(value):
    return value


query = ObjectType("Query")
query.set_field("listBackups", listBackups_resolver)
query.set_field("getBackup", getBackup_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers, datetime_scalar
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    print(data)
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    #print(result)
    return jsonify(result), status_code