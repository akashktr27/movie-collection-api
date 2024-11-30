import os
import json
import logging
import random
import uuid
import string

def generate_uuid():
    return str(uuid.uuid4())
def generate_random_text(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length))

def read_json_file(file_name):
    file_path = os.path.join('features/'+file_name)

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            data['title'] = generate_random_text(10)
            for movie in data['movies']:
                movie['uuid'] = generate_uuid()

        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON in file '{file_path}': {e}")
        return None
    except Exception as e:
        print(f"Unexpected error reading file '{file_path}': {e}")
        return None

def before_all(context):
    context.shared_data = {}
    print("setting up resources before all tests")
    log_file_path = os.path.join(os.getcwd(), "integraton_test.log")

    #set up logger and handle file
    logger = logging.getLogger("onefin API testing")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("Starting behave tests with file handler")

    context.logger = logger
    data = read_json_file("payload.json")
    put_data = read_json_file("put_payload.json")
    context.collection = data
    context.put_payload = put_data

def after_all(context):
    print("Tearing all resources after all tests")

def before_scenario(context, scenario):
    context.logger.info(f"Starting scenario: {scenario.name}")

def after_scenario(context, scenario):
    context.logger.info(f"Finished scenario: {scenario.name}")
