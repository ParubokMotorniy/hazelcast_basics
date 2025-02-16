import hazelcast
import os
from time import process_time_ns
import sys

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
    cluster_name=f"{sys.argv[1]}", 
    ) 
    map = client.get_map("map-increment").blocking()
    key = "conflict-pessimistic"
    map.put_if_absent(key, 0)

    my_pid = os.getpid()

    print(f"\n-----[{my_pid}][Starting pessimistic incrementation]-----\n")

    total_map_interaction_time = 0
    for i in range(10000):
        increment_start = process_time_ns()
        map.lock(key)

        try:
            current_value = map.get(key)
            current_value += 1
            map.put(key, current_value)
        finally:
            map.unlock(key)
        increment_end = process_time_ns()
        total_map_interaction_time += increment_end - increment_start

    print(f"\n-----[{my_pid}][Pessimistic incrementation finished]-----\n")
    print(f"\n-----[{my_pid}][Total map interaction time (ms): {total_map_interaction_time / 1000000}]-----\n")

    client.shutdown()

