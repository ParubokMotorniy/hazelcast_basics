import hazelcast
import threading
import os

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
    cluster_name="hazelcast-test", 
    )
    queue = client.get_queue("bounded-queue-test").blocking()
    my_pid = os.getpid()

    def consume_items():
        while True:
            queue_head = queue.take()
            if queue_head == "null":
                print(f"-----[{my_pid}][Consumer terminated]-----")
                break
            print(f"-----[{my_pid}][Consumed item: {queue_head}]-----")

    consumer_thread = threading.Thread(target=consume_items, name="Consumer")
    consumer_thread.start()
    consumer_thread.join()

    client.shutdown()