class DbMeta(type):
    def __new__(cls, name, bases, attrs):
        cls.__makeVars = {'val1': 'v1', 'val2': 'v2'}
        return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        cls.__SetAttributes(cls, name)
        #setattr(cls, 'Secret', property(lambda cls: attrs['_{0}__secret'.format(name)])) # Db.Secretプロパティ定義

    @classmethod
    def __SetAttributes(cls, target, name):
        for key, val in cls.__makeVars.items():
            setattr(target, '_{0}__{1}'.format(name, key), val) # Db.Secretプロパティ定義
            setattr(target, key, property(lambda target: getattr(target, '_{0}__{1}'.format(name, key)))) # Db.Secretプロパティ定義
            """
            #注意！以下のようにするとプロパティ返却値がすべて同一になってしまう！なぜ？
            varname = '_{0}__{1}'.format(name, key)
            setattr(target, varname, val) # Db.Secretプロパティ定義
            setattr(target, key, property(lambda target: getattr(target, varname))) # Db.Secretプロパティ定義
            """

        for key, val in cls.__makeVars.items():
            print(key, getattr(target, key), getattr(target(), key))

