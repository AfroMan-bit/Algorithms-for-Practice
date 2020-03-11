 # def reverseStr(someString):
#     newstring = ""
#     for i in range(len(someString)-1, -1, -1):
#         newstring += someString[i]  
#     return newstring
# print(reverseStr("hello"))


# def validation (string):
#     open = 0
#     close = 0
#     for i in range (len(string)):
#         if string[i] == "(":
#             open += 1
#         elif string[i] == ")":
#             close += 1
#         if close > open:
#             return("invalid")
#     if open == close:
#         return True
#     if open != close:
#         return False
# print(validation("(())"))


# def bracesValid(string):
#     parens = 0
#     brace = 0
#     bracket = 0
#     arr = []
#     for i in range(len(string)):
#         if string[i] == "(":
#             parens +=1
#             arr.append(string[i])
#         if string[i] == ")":
#             parens -=1
#             if arr[len(arr)-1] == "(":
#                 arr.pop()
#         if string[i] == "{":
#             brace +=1
#             arr.append(string[i])
#         if string[i] == "}":
#             brace -=1
#             if arr[len(arr)-1] == "{":
#                 arr.pop()
#         if string[i] == "[":
#             bracket +=1
#             arr.append(string[i])
#         if string[i] == "]":
#             bracket -=1
#             if arr[len(arr)-1] == "[":
#                 arr.pop()
        
#         if parens < 0 or brace < 0 or bracket < 0:
#             print("premature closing symbol")
#             return False
#     if parens != 0 or brace != 0 or bracket !=0:
#         print("uneven amount of matching symbols")
#         return False
#     elif len(arr) > 0:
#         print("symbols not in valid order")
#         return False
#     else:
#         return True

# bracesValid("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!")
# bracesValid("D(i{a}1[ t]o)n{e")
# bracesValid("A(1)s[0(n]0{t) 0}k")
# bracesValid("(){}[]")
# bracesValid("(}")
# // bracesValid("[(])") // false 3
# bracesValid("()[(])")
# bracesValid("{}[[(({({{}}})[))]]]")



# def palindrome(someword):
#     for i in range(len(someword)//2):
#         if someword[i] != someword[len(someword)-i-1]:
#             return False
#     return True

# print(palindrome("racecar"))
# print(palindrome("hello"))
# print(palindrome("tacocat"))


# def bookIndex(pages):
#     result = str(pages[0])
#     prev = pages[0]
#     for i in range(1, len(pages)):
#         if prev + 1 == pages[i]: 
#             if result[-1] != "-":
#                 result += "-"
#         else:
#             if result[-1] != "-":
#                 result += ", " + str(pages[i])
#             else:
#                 result += str(pages[i-1]) + ", "  
#         if result[-1] == " ":
#             result += str(pages[i])

#         print("{} | {}".format(i, result)) 
#         prev = pages[i]
#     return result

# print(bookIndex([1,2,3,8,15,16,17,21]))

# LISTING LIST


# class Node:
#     def __init__(self, val):
#         self.value = val
#         self.next = None

# class SLL:
#     def __init__(self):
#         self.head = None

# def addfront(self, val):
#     # soluion to add a node to front of SLL here below
#     # create a new node
#     newNode = Node(val)
#     newNode.next = self.head
#     self.head = newNode
#     return self

# def contains(self, val):
#     # solution to contains in SLL here below
#     runner = self.head
#     # print("***** printing runner below")
#     # print(runner)
#     while runner != None:
#         if runner.value == val:
#             return True
#         runner = runner.next
#     return False

# def removefront(self):
#     if self.head != None:
#         self.head = self.head.next
#     else:
#         return None

# def length(self):
#     lengthcount = 0
#     runner = self.head
#     while runner != None:
#         lengthcount += 1
#         runner = runner.next
#     return lengthcount

# def display(self):
#     mylist = ""
#     runner = self.head
#     while runner != None:
#         mylist += runner.value+"_"
#         runner = runner.next
#     return mylist


# newSLL = SLL()
# newSLL.addfront(5)
# newSLL.addfront(15)
# newSLL.addfront(6)
# newSLL.addfront(3)
# print(newSLL)
# print(newSLL.contains(3))
# print(newSLL.contains(51))

# def appendVal(self, val,x):
#     runner = self.head
#     while runner != None:
#         if runner.value == x:
#             temp= runner.next
#             new_Node= Node(val)
#         runner.next = new_Node
#         new_Node.next = temp
#         return "_"
#     runner = runner.next
#     return f"{x}"


# def prependVal(self, val, x):
#     runner = self.head
#     while runner != None:
#         if runner.next.value == x:
#             temp = runner.next
#             new_Node = Node(val)
#             runner.next = new_Node
#             new_Node.next = temp
#             return "val prep"
#         runner= runner.next
#     return "f{x} not found"


# def max_last(self):
#     max_val = self.head.value
#     prev = self.head
#     runner = self.head
#     while runner.next != None:
#         if max_val < runner.next.value
#             max_val = runner.next.value
#             prev = runner
#         runner = runner.next
#     runner.next = Node(max_val)
#     prev.next = prev.next.next
    

# def minfront(self):
#     runner = self.head
#     min = self.head.value
#     prev = self.head
#     while runner.next != None
#         if runner.next.value.value < min:
#             min = runner.next.value
#             prev = runner
#         runner = runer.next
#         addfront (min)
#         prev.next = prev.next.next


# def max(self):
#     runner = self.head
#     max = self.head.value
#         prev = self.head
#     while runner.next != None:
#         if runner.next != None:
#             max = runner.next.value
#             prev = runner
#         if runner.next.value == None:
#             if prev = self.head
#                 self.head = self.head.next
#                 runner.next = Node(max)
#             else:
#                 prev.next = self.next.next
#                 runner.next == Node()


# QUEUES AND STACKS

class Node:
    def__init__(self,val):
        self.value = val
        self.next = None

class queue:
    def__init__(self):
            self.head = None
        self.tail = None
    def contains(val):
        runner = self.head
        while runner.value != None:
            if runner.value == val:
                return True
            else:
                runner = runner.next
        return False


def enqueue(val):
    if self.head.value == None:
        self.head = Node(val)
        self.tail = self.head
    else:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode

    
def dequeue():
    self.head = self.head.next
        return self.head.val

    
def front():
    return self.head.value


def empty():
    if self.head == None:
        if self.tail == None:
            return True
        else:
            return False

def size():
    count = 0
    runner = self.head
    while runner != None
        count + 1
        runner = runner.next
    return count






    







