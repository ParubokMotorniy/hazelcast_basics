#!/bin/sh

python3 ./queue_consumer.py &
python3 ./queue_consumer.py &
python3 ./queue_producer.py &