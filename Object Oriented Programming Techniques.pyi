'''
Inherittance
'''

'''
Consider we have two classes and we want to re-use the methods we have defined in the first class in the second one.
The tedious way would  be to redefine them again. But such a technique is not efficient as we rewrite the same block 
of code and use a redundant space of memory. Therefore, it would be efficient to 'inherit' the methods of the first 
class (parent class) to the second class (child class).
'''

#e.g.
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username

  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

class Admin(User):
  def edit_message(self,message, new_text):
    message.text = new_text

symeon = User("SymPas")
message = Message("Symeon", "Alex", "You talk too much.")



'''
In the above example the class 'Admin' (child class) inherits the methods and attributes of the class 'User'
(parent class). Observe that we have also used the overriding technique for the method  'edit_message'. Overriding 
 can can be used to add some further functionality in the methods of the parent class within the child class. 
'''


'''
Inheritance and super()
'''

'''
class Name:
    def __init__(self, *parameters):
        self.parameters = parameters
        
    def method1(*vars):
        #do some stuff
        pass
    
    def method2(*vars2):
        #do some stuff
        pass
    
class  Child_class(Name):
    def __init__(self, *parameters, new_variable = None):
        super().__init__(*parameters)
        self.new_variable = new_variable
    
    def method1(*vars):
        #do other stuff
        pass
    
    def method2(*vars2):
        #do some other stuff
        pass
'''



'''
Interface
'''

'''
What if we want to use different instances of the same object but each of these objects should perform different tasks?
That's where the idea of the 'Interface' technique we create a parent class and different subclasses that will
accept same name methods but will perform different tasks within each subclass.
'''


#e.g.
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return .001*self.price_of_insured_item


class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return .00005*self.price_of_insured_item


'''
Other dunder methods
'''

'''
__repr__(self) #returns a string 
__iter__(self) #returns an iterable object, that can be a an element of a list, tuple, dictionary 
__len__(self) #returns the length of a one dimensional object (list, tuple, dictionary)
__add__(self, other) #returns the addition of two objects 
'''


