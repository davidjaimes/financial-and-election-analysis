# Make Class to Write Print Functions to Console and Text File.
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('budget_data_djaimes.txt', 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
sys.stdout = Logger()
