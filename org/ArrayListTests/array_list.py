class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.cap = 4
        self.arr = [0] * self.cap
        self.size = 0
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = str(self.arr[0])
        for i in range(1, self.size):
            return_string += ', ' + str(self.arr[i])
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.needs_resize()
        for i in range(self.size-1, -1, -1):
            self.arr[i+1] = self.arr[i]
        self.arr[0] = value
        self.size += 1
        self.ordered = False

    def needs_resize(self):
        if self.size == self.cap:
            self.resize()

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        self.needs_resize()
        if index == 0:
            self.prepend(value)
        elif index < self.size:
            for i in range(self.size - 1, index-1, -1):
                self.arr[i+1] = self.arr[i]
            self.arr[index] = value
            self.size += 1
        elif index == self.size:
            self.append(value)
        else:
            print('wrong index!!!')
        self.ordered = False

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.needs_resize()
        self.arr[self.size] = value
        self.size += 1
        self.ordered = False

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self.arr[index] = value
        self.ordered = False

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        temp = [0] * self.cap * 2
        for i in range(self.size):
            temp[i] = self.arr[i]
        self.cap *= 2
        self.arr = temp

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def clear(self):
        self.arr = [0] * self.cap
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    print(str(arr_lis))