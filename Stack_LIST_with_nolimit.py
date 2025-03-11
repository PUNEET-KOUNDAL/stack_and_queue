class Stack :
    def __init__(self):
        self.list=[ ]


    def __str__(self):
        value = self.list[ : :-1]
        value = [str(x) for x in value]
        return "\n".join(value)
    
    def push(self , value ) :
        self.list.append(value)
        return "element pushed successfully"
    
    def isEmpty(self) :
        return  len(self.list) == 0 
        
    def pop(self) :
        if self.isEmpty():
            return "stack is empty"
        return self.list.pop()
    
    def peek (self):
        if self.isEmpty():
            return "stack is empty"
        return self.list[len(self.list)-1]
    
    def delete(self):
        if self.isEmpty():
            return "stack is empty"
        else :
            self.list = []
            return "stack deleted successfully"