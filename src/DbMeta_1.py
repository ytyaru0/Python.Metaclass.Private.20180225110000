class DbMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['_{0}__secret'.format(name)] = 'my_secret' # Db.__secret 定義
        return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        setattr(cls, 'Secret', property(lambda cls: attrs['_{0}__secret'.format(name)])) # Db.Secretプロパティ定義
