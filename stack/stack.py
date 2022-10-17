'''
Create a stack of numbers

PSEUDOCODE
----------
1. Create a class
2. Create an array of fixed length
3. Create a push method - Add to the back
4. Create a pop method - Remove from the back
5. Create a peek method - Show item at the top
. 
'''

class MyStack:
    myList = [0] * 5
    back = 0
    
    @classmethod
    def push(cls, num):
        if cls.back < len(cls.myList) and cls.back > -1:
            cls.myList[cls.back] = num
            cls.back += 1
        else: 
            print("Stack is full")
            return -1
            

    
    @classmethod
    def pop(cls):
        if  cls.back > -1 and cls.back < len(cls.myList):
            currentNum = cls.myList[cls.back - 1]
            cls.myList[cls.back - 1] = 0
            cls.back -= 1
            return currentNum
        else: 
            cls.back = 0
            print("Stack is empty")
            return -1

    @classmethod
    def peek(cls):
        if cls.back > -1 and cls.back < len(cls.myList):
            return cls.myList[cls.back - 1]
        else: return -1

MyStack.push(7)
MyStack.push(7)   
MyStack.push(5)  
MyStack.pop() 
MyStack.push(6)   
MyStack.push(3)  
MyStack.pop() 
MyStack.pop() 
MyStack.pop() 
MyStack.pop() 
# MyStack.pop() 

# print(MyStack.pop() 
# )

MyStack.push(2)   
MyStack.push(7)
MyStack.push(4)
MyStack.pop() 
MyStack.pop() 
MyStack.pop()    
MyStack.pop()  
MyStack.push(9)   









print(MyStack.myList)