import hazelcast
import threading
import os

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
    cluster_name="hazelcast-test", 
    )
    queue = client.get_queue("bounded-queue-test").blocking()
    num_consumers = 2
    my_pid = os.getpid()

    def put_items():
        for i in range(100):
            queue.put(f"item_#{i}")
            print(f"-----[{my_pid}][Enqueued item #{i}]-----")
        for i in range(num_consumers):
            queue.put("null")
            print(f"-----[{my_pid}][Poison pill #{i} injected]-----")

        print(f"-----[{my_pid}][Producer terminated]-----")
    
    offer_thread = threading.Thread(target=put_items, name="Producer")

    offer_thread.start()
    offer_thread.join()

    client.shutdown()

