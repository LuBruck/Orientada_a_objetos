from log import LogPrint

# class Eletronico:
#     def __init__(self):
#         self.nome = None
#         self._ligado = None

#     def ligar(self):
#         if not self._ligado:
#             self._ligado = True
    
#     def desligar(self):
#         if self._ligado:
#             self._ligado = False
    
# class Celular(Eletronico, LogPrint):
#     def ligar(self):
#         super().ligar()
#         self.log_succes('AIAIAIAI')

#     def desligar(self):
#         super().desligar()
#         self.log_error("saiu, coco")



# sungui = Celular()
# sungui.ligar()
# print(sungui._ligado)

# sungui.desligar()

# print(sungui._ligado)





###############################################################################################


  
class Eletronico:
    def __init__(self):
        self.nome = None
        self._ligado = None

    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False
    
class Celular:
    def __init__(self):
        self._Eletronico = Eletronico()
        self._LogPrint = LogPrint()

    def ligar(self):
        self._Eletronico.ligar()
        self._LogPrint.log_succes('AIAIAIAI')

    def desligar(self):
        self._Eletronico.desligar
        self._LogPrint.log_error("saiu, coco")
      

        
suaaa = Celular()
suaaa.ligar()
print(suaaa._Eletronico._ligado)
