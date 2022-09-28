class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    def __str__(self):
        return '<Instance of %s(%s), address %s:\n%s>' % (
            self.__class__.__name__, # My class's name
            self.__supers(), # My class's own supers
            id(self), # My address
            self.__attrnames()) # name=value list
    def __supers(self):
        names = []
        for super in self.__class__.__bases__: # One level up from class
            names.append(super.__name__) # name, not str(super)
        return ', '.join(names)
    # Or: ', '.join(super.__name__ for super in self.__class__.__bases__)
