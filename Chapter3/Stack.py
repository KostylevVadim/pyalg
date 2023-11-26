class Stack:
    def __init__(self, list = []):
        self.__list = list
        self.__len = len(list)
    def __str__(self):
        s= 'Content of Stack '
        for elem in self.__list:
            s+=str(elem)+' '
        s+= '\nLength '+ str(self.__len)
        return s
    def push(self, elem):
        self.__list.append(elem)
        self.__len+=1
    
    def pop(self):
        if len(self.__list) == 0:
            return None

        a = self.__list.pop()
        self.__len = len(self.__list)
        
        return a
    
    def peek(self):
        x= self.__list[-1]
        return x
    
    def isEmpty(self):
        return self.__len == 0
    
    def size(self):
        return self.__len