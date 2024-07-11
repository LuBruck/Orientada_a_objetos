#Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f"Error: {msg} {self.__class__.__name__}")
        
    def log_succes(self, msg):
        return self._log(f"Succes: {msg} {self.__class__.__name__}")


class LogPrint(Log):
    def _log(self, msg):  #se eu tirar esses 2, e chamar ._log em um Logprint, vai dar o raise NotImplemetedError
        print(f'{msg} ({self.__class__.__name__}) ')

class LogFile(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__}) '

        with open(LOG_FILE , 'a') as arquivo:
            arquivo.write(f'{msg_formatada}\n')

if __name__ == '__main__':
    lp = LogPrint()
    lp.log_error("aiiiiii calica")

    lf = LogFile()
    lf.log_succes("QUIDILICAA")
    # lf._log('UIUIUIUI')
