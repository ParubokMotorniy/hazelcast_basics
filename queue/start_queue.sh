#!/bin/sh

cluster_name="$1"

python3 ./queue_consumer.py "${cluster_name}" &
python3 ./queue_consumer.py "${cluster_name}" &
python3 ./queue_producer.py "${cluster_name}" &