
class Stack:

    # A constructor that initialises an empty stack
    def __init__(self):
        self.elements = []

    # Push item on the Stack 
    def push(self,item):
        self.elements.append(item)
        

    # Pop the Stack 
    def pop(self):
        return self.elements.pop()
        

    # Check if the Stack has any items
    def isEmpty(self):
        if (len(self.elements) > 0):
            return False
        else:
            return True
        


def main():
    s = Stack()
    s.push(4)
    s.push(9)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print('Stack is empty',s.isEmpty())
    s.pop()
    print('Stack is empty',s.isEmpty())
    
if __name__ == '__main__':
    main()