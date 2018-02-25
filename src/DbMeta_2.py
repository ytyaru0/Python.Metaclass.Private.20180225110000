class DbMeta(type):
    def __new__(cls, name, bases, attrs):
        c = type.__new__(cls, name, bases, attrs)
        setattr(c, '_{0}__secret'.format(name), 'my_secret')
        setattr(c, 'Secret', property(lambda c: getattr(c, '_{0}__secret'.format(name))))
        return c

    def __init__(cls, name, bases, attrs): pass

