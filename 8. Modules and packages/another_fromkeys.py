class new_dict(dict):
    def __init__(self):
        super(new_dict, self).__init__()

    @staticmethod
    def another_fromkeys(iterable, function):
        d = {}
        for x in iterable:
            d[x] = function(x)
        return d
