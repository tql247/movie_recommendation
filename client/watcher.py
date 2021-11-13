import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import requests
from config import computer_name

def get_path_to_watch():
    url = "http://localhost:5000/source/source_path?created_by=" + computer_name
    
    payload={}
    headers = {}
    print(url)

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response)
    print(response.text)


class Event(LoggingEventHandler):
    def on_created(self, event):
        # print("Foaaaobar123123123")
        file_path = event._src_path
        file_name = os.path.basename(file_path)
        if file_name not in list_file_name:
            print("add video to database")
            print(file_name)
            list_file_name.append(file_name)
        else:
            # print("add video to database")
            list_file_name.remove(file_name)


    def on_modified(self, event):
        pass


list_file_name = []


if __name__ == "__main__":
    # get_path_to_watch()

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    path = r'\\14.241.228.138\storage\linhtest'
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(5)
    finally:
        observer.stop()
        observer.join()