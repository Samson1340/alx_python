class Base:
    '''A representation of the base.'''

    __nb_objects = 0

    def _init_(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = Base.__nb_objects