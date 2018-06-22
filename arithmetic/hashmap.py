import random
import math

# 实现jdk1.7的HashMap


class HashMap:
    def __init__(self):
        self.__table = []
        # 负载因子
        self.__loadFactor = 0.5
        # 键值对的总数量
        self.__size = 0
        # 表格数组空闲的格子大小
        self.__table_busy_size = len(self.__table)

    def table(self):
        return self.__table

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size() == 0

    def containsKey(self, key):
        pass

    def containsValue(self, key):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        if self.size() == 0 or self.__get_current_load_factor() > self.__loadFactor:
            self.__resize()
        index = self.__hash(key) % len(self.__table)
        if self.__table[index]:
            node = self.__table[index]
            while node:
                if node.key == key:
                    node.value = value
                    break
                if node.next == None:
                    node.next = Entry(self.__hash(key), key, value, None)
                    self.__size += 1
                    break
                node = node.next
        else:
            entry = Entry(self.__hash(key), key, value, None)
            self.__table[index] = entry
            self.__size += 1
            self.__table_busy_size += 1

    def clear(self):
        pass

    def putAll(self, map):
        pass

    def remove(self, key):
        pass

    def __get_current_load_factor(self):
        length = len(self.__table)
        if length == 0:
            return 0
        result = self.__table_busy_size / length
        return result

    def __scan_entry(self, entry, new_table, new_table_size):
        table_busy_size = 0
        if entry.next:
            table_busy_size += self.__scan_entry(entry,
                                                 new_table, new_table_size)
            entry.next = None
        else:
            index = self.__hash(entry) % new_table_size
            if new_table[index]:
                node = new_table[index]
                while node:
                    node = node.next
                node.next = entry
            else:
                new_table[index] = entry
                table_busy_size += 1
        return table_busy_size

    def __link_table_to_list(self, entry):
        list = []
        node = entry
        while node:
            list.append(node)
            node = node.next

    def __resize(self):
        new_table_size = 2
        if len(self.__table) > 0:
            new_table_size = 2 * len(self.__table)
        new_table = [None] * new_table_size
        new_table_busy_size = 0
        for entry in [e for e in self.__table]:
            new_table_busy_size += self.__scan_entry(
                entry, new_table, new_table_size)

        self.__table = new_table
        self.__table_busy_size = new_table_busy_size

    def __hash(self, obj):
        return hash(obj)


class Entry:
    def __init__(self, h, k, v, n):
        self.hash = h
        self.key = k
        self.value = v
        self.next = n


if __name__ == "__main__":
    # list = [random.randint(1, 1000) for i in range(20)]
    # print(list)
    # print([x % 2 for x in list])
    # print([x % 4 for x in list])
    # print([x % 8 for x in list])
    # print([x % 16 for x in list])
    # print([x % 32 for x in list])
    map = HashMap()
    map.put('a', 'a')
    map.put('b', 'b')
    map.put('c', 'c')
    map.put('d', 'd')
    map.put('e', 'e')
    map.put('f', 'f')
    map.put('g', 'g')
    map.put('h', 'g')
    map.put('i', 'i')

    print(map.table())
    # map.put('a', 1)
    # map.put('a', 1)
    # map.put('a', 1)
    # map.put('a', 1)
