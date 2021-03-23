import array

class ArrayList:

    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)
    
    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def prepend(self, value):
        if self.length == self.capacity: #if it is full
            new_arr = array.array('l', [0]*self.capacity*2)
            self.capacity *= 2
        else:
            new_arr = array.array('l', [0]*self.capacity)
            new_arr[1:self.length+1] = self.array[:self.length]

        new_arr[1:self.length+1] = self.array[:self.length]
        new_arr[0] = value
        self.length += 1
        self.array = new_arr

    def append(self, value):
        if self.length == self.capacity: # if it is full
            new_arr = array.array('l', [0]*self.capacity*2)
            self.capacity *= 2
        else:
            new_arr = array.array('l', [0]*self.capacity)
        
        new_arr[:self.length] = self.array[:self.length]
        new_arr[self.length] = value
        self.length += 1
        self.array = new_arr
            

    def set_head(self, index):
        if index >= self.capacity or index < 0:
            print("not valid index, please put 0 to capacity-1")
        else:
            new_arr = array.array('l', [0]*self.capacity)
            new_arr[:index] = self.array[index:]
            self.array = new_arr
            self.length -= index

    def access(self, index):
        if index >= self.capacity or index < 0:
            print("not valid index, please put 0 to capacity-1")
        else:
            return self.array[index]

    def insert(self, index, value):
        if index > self.length or index < 0:
            print('please put index 0 to ArrayList\'s length')
        else:
            if index == self.length:
                ArrayList.append(self, value)
            elif index == 0:
                ArrayList.prepend(self, value)
            else:
                if self.length == self.capacity: # if it is full
                    new_arr = array.array('l', [0]*self.capacity*2)
                    self.capacity *= 2
                else:
                    new_arr = array.array('l', [0]*self.capacity)

                new_arr[:index] = self.array[:index]
                new_arr[index] = value
                new_arr[index+1:] = self.array[index:]
                self.array = new_arr
                self.length += 1

    def remove(self, index):
        if index > self.length or index < 0:
            print('please put index 0 to ArrayList\'s length')
        else:
            new_arr = array.array('l', [0]*self.capacity)
            new_arr[:index] = self.array[:index]
            new_arr[index:] = self.array[index+1:]
            self.array = new_arr
            self.length -= 1

    def print(self):
        for i in range(self.length):
            print(self.array[i], end = ' ')
        print()
        
        
        

arr_list = ArrayList(4)

# check if list is empty
print('arr_list is empty? :',ArrayList.is_empty(arr_list))

# put values
for i in range(1, 5):
    ArrayList.prepend(arr_list, i)

# print
print("-----------------prepand----------------")
print('Input Order [1,2,3,4] : ' , end = '')
ArrayList.print(arr_list)

# put value
ArrayList.prepend(arr_list, 5)
print('After put value 5 it\'s capacity grow up! arr_list\'s capacity :', arr_list.capacity)
ArrayList.print(arr_list)


print("-----------------append----------------")
# put value
for i in range(6, 9):
    ArrayList.append(arr_list, i)

print('Input Order [6,7] :' , end = ' ')
ArrayList.print(arr_list)

ArrayList.append(arr_list, 9)
print('After put value 9 it\'s capacity grow up! arr_list\'s capacity :', arr_list.capacity)
ArrayList.print(arr_list)

print("-----------------set head----------------")

print('if setting head at index "-1" : ', end = '')
ArrayList.set_head(arr_list, -1)

ArrayList.set_head(arr_list, 5)
print('After setting head at index "5" : ', end = '')
ArrayList.print(arr_list)
print('arr_list length : ', arr_list.length)
print('arr_list capacity : ', arr_list.capacity)

print("-----------------access----------------")

print('if index is wrong : ', end = '')
ArrayList.access(arr_list, -1)

print('Accessing at second element', ArrayList.access(arr_list, 1))

print("-----------------insert----------------")

print('Insert value at -1 :', end = '')
ArrayList.insert(arr_list, -1, 0)

print('Insert value 5 at first :', end = '')
ArrayList.insert(arr_list, 0, 5)
ArrayList.print(arr_list)

print('Insert value 10 at last :', end = '')
ArrayList.insert(arr_list, arr_list.length, 10)
ArrayList.print(arr_list)

print('Insert value 100 at second position : ', end = '')
ArrayList.insert(arr_list, 1, 100)
ArrayList.print(arr_list)

print("-----------------remove----------------")

print('Remove first one : ', end = '')
ArrayList.remove(arr_list, 0)
ArrayList.print(arr_list)

print('Remove last one : ', end = '')
ArrayList.remove(arr_list, arr_list.length-1)
ArrayList.print(arr_list)

print('Remove second one : ', end = '')
ArrayList.remove(arr_list, 1)
ArrayList.print(arr_list)