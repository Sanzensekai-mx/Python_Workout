class FlexibleDict(dict):
    def __getitem__(self, item):
        try:
            if item in self:
                pass
            elif str(item) in self:
                item = str(item)
            elif int(item) in self:
                item = int(item)
        except ValueError:
            pass
        return dict.__getitem__(self, item)


new_dict = FlexibleDict({1: 2, '3': 23, 'ad': 4, '12': 2})


# print(new_dict[3])
# print(new_dict[12])
# print(new_dict['1'])


# EX41_2

class StringKeyDict(dict):
    def __setitem__(self, key, value):
        return dict.__setitem__(self, str(key), value)


skd = StringKeyDict()
skd[1] = 10


# print(skd['1'])

# EX41_2

class RecentDict(dict):

    def __init__(self, recent):
        super(RecentDict, self).__init__()
        self.recent = recent
        self.current_keys = []

    def __setitem__(self, key, value):
        self.current_keys.append(key)
        if len(self) == self.recent:
            del self[self.current_keys[0]]
            del self.current_keys[0]
        return dict.__setitem__(self, key, value)


rd = RecentDict(3)
rd[1] = 1
rd['2'] = 2
rd['3'] = 3
rd[4] = 4
rd[5] = 5
# print(rd.current_keys)
# print(rd)
rd[6] = 6
# print(rd.current_keys)
# print(rd)
rd[7] = 7


# print(rd.current_keys)
# print(rd)

# EX41_3

class FlatList(list):
    def append(self, val):
        try:
            for i in iter(val):
                list.append(self, i)
        except TypeError:
            list.append(self, val)
            # print(val)


list_ = FlatList()
list_.append([1, 2, 3])
list_.append(4)
print(list_)
