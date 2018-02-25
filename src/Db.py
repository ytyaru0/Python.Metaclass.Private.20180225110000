from DbMeta import DbMeta 
class Db(metaclass=DbMeta):
    def show(self):
        print('----- Db.show(self) -----')
        print(dir(self))
        #print(self.__secret)
        #print(self._Db__secret)
        #print(self.Secret)
        #assert(hasattr(self, '_Db__secret')) # self.__secret
        #assert(hasattr(self, 'Secret')) # self.Secret
