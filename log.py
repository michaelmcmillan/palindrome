from datetime import datetime

class Log:

    @classmethod
    def stdout(cls, message):
        print('%s: %s' % (datetime.now(), message))
