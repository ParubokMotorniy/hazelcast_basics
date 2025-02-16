import hazelcast
import os
import sys

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
    cluster_name=f"{sys.argv[1]}", 
    ) 
    map = client.get_map("map-increment").blocking()
    key = "conflict"
    map.put_if_absent(key, 0)

    my_pid = os.getpid()

    print(f"\n-----[{my_pid}][Starting concurrent incrementation]-----\n")

    for i in range(10000):
        current_value = map.get(key)
        current_value += 1
        map.put(key, current_value)

    print(f"\n-----[{my_pid}][Concurrent incrementation finished]-----\n")

    client.shutdown()

