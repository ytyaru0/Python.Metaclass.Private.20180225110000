class DbMeta(type):
    ClassValue = 'Class-Value'
    def __new__(cls, name, bases, attrs):
        cls.clsval = 'cls-val'
        cls.__Method(cls)
        cls.__ClassMethod()
        attrs['_{0}__secret'.format(name)] = 'my_secret' # Db.__secret 定義
        return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        cls.__Method()
        cls.__ClassMethod()
        setattr(cls, 'Secret', property(lambda cls: attrs['_{0}__secret'.format(name)])) # Db.Secretプロパティ定義

    def __Method(cls):
        print('__Method', cls, cls.ClassValue, cls.clsval)

    @classmethod
    def __ClassMethod(cls):
        print('__ClassMethod', cls, cls.ClassValue, cls.clsval)
