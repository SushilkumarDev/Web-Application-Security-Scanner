import threading
from queue import Queue

class ConcurrentScanner:
    def __init__(self, urls, scanner):
        self.urls = urls
        self.scanner = scanner
        self.queue = Queue()

    def worker(self):
        while not self.queue.empty():
            url = self.queue.get()
            self.scanner.run_scans([url])
            self.queue.task_done()

    def start(self, num_threads=5):
        for url in self.urls:
            self.queue.put(url)

        for _ in range(num_threads):
            t = threading.Thread(target=self.worker)
            t.start()

        self.queue.join()
        print("Concurrent scanning completed")
