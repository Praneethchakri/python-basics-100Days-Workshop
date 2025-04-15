import threading


class MyThread(threading.Thread):
    def run(self):
        print("Thread Started..")


thread = MyThread()
thread.start()
thread.join()
