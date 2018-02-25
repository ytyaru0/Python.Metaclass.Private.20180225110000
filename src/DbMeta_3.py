class DbMeta(type):
    def __new__(cls, name, bases, attrs):
        return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        setattr(cls, '_{0}__secret'.format(name), 'my_secret')
        setattr(cls, 'Secret', property(lambda cls: getattr(cls, '_{0}__secret'.format(name))))

