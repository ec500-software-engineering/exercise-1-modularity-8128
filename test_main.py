import modules.InputModule
import modules.StorageModule
import modules.AlertModule
import modules.UserInterfaceModule
import modules.AiModule
import queue
import threading


def test_func():
    main()


def main():
    q1 = queue.Queue()
    q2 = queue.Queue()
    q3 = queue.Queue()
    ipt = threading.Thread(target=modules.InputModule.InputModule, args=(q1))
    storage = threading.Thread(target=modules.StorageModule.Storage, args=(q1))
    getIput = threading.Thread(target=modules.StorageModule.Storage.getIput,
                               args=("bo"))
    alert = threading.Thread(target=modules.AlertModule.Alert, args=(q1, q2))
    ai = threading.Thread(target=modules.AiModule.AIModule, args=(q1, q3))
    ui = threading.Thread(target=modules.UserInterfaceModule.UserInterface,
                          args=(q1, q2, q3))
    ipt.start()
    storage.start()
    getIput.start()
    alert.start()
    ai.start()
    ui.start()
    ipt.join()
    storage.join()
    getIput.join()
    alert.join()
    ai.join()
    ui.join()


if __name__ == '__main__':
    main()
