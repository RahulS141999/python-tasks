#app.py
import logging
from flask import Flask


app = Flask(__name__)


logging.basicConfig(filename='production.log', level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s - %(message)s')


@app.route('/')
def hello():
    name = "yash"
    logging.info(f"Hello, {name}! request to the / endpoing received.")
    return f"Hello, {name}"


@app.route('/about')
def about():
    logging.info("request to /about endpoing received")
    return "this is about page"


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5002)

# cmd = "gunicorn app:app -b 0.0.0.0:5000"

#time_consuming.py
import logging
import time

logging.basicConfig(filename='task20/performance.log',
                    level=logging.INFO,
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )


def time_consuming_operation():

    start_time = time.time()

    result = 0
    for i in range(1, 1000):
        result += i

    execution_time = time.time() - start_time
    processing_speed = result/execution_time

    logging.info(
        f"time consuimg operation took {execution_time} seconds. Result: {result}")
    logging.info(f"processing speed : {processing_speed} unit/s")


if __name__ == '__main__':

    time_consuming_operation()

    logging.info("End of program")
