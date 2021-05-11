import threading
class CdbTaskThread(threading.Thread):
    def __init__(self, city, name = ''):
        super(CdbTaskThread, self).__init__(name = name)
        self.city = city

    def init(self):
        self.cdbTaskDb = 1


test_thread = CdbTaskThread('test1',name='test_thread')
test_thread.init()
test_thread.start()