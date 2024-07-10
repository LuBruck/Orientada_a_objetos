#Abstração
class Log:
    def log(self, msg):
        print(__name__)
        raise NotImplementedError('Implemente o método log')


if __name__ == '__main__':
    l = Log()
    l.log('penis')