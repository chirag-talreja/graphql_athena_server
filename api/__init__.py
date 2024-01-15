from flask import Flask
from flask_cors import CORS
from urllib.parse import quote_plus

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# define connection
conn_str = 'awsathena+rest://{aws_access_key_id}:{aws_secret_access_key}@athena.{region_name}.amazonaws.com:443/{' \
           'schema_name}?s3_staging_dir={s3_staging_dir} '

app.config["SQLALCHEMY_DATABASE_URI"] = conn_str.format(
    aws_access_key_id='<>',  # shared across the entire org
    aws_secret_access_key='<>',  # shared across the entire org
    region_name='<>',  # shared across the entire org
    schema_name='<>',
    s3_staging_dir='<>'
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
athena_connection = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello"
