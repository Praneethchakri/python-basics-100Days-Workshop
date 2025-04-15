import threading


def access_Thread():
    print("Thread-1 start")


def access_Thread2():
    print("Thread-2 Start")


thread = threading.Thread(target=access_Thread())
thread.start()
thread.join()

thread = threading.Thread(target=access_Thread2())
thread.start()
thread.join()
