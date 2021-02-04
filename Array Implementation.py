class myArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __str__(self) -> str:
        return str(self.data)
    
    def get(self, index):
        return self.data[index]

    def push(self, value):
        self.data[self.length] = value
        self.length += 1
        return self.length
    
    def pop(self):
        deleted = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return deleted
    
    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        
        del self.data[self.length - 1]
    
    def delete(self, index):
        deleted = self.data[index]
        self.shift_items(index)
        self.length -= 1
        return deleted
    
    


newArray = myArray()
newArray.push(1)
newArray.push(2)
newArray.push(3)
newArray.push(4)
newArray.push(5)

print(newArray)
newArray.delete(2)
print(newArray)
