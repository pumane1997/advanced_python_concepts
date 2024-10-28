
'''
Object-Oriented Programming in Python
In Object-Oriented Programming (OOP), we define classes that act as blueprints to create 
objects in Python with attributes and methods (functionality associated with the objects).

This is a general syntax to define a class:

class <ClassName>:

    <class_attribute_name> = <value>

    def __init__(self,<param1>, <param2>, ...):
        self.<attr1> = <param1>
        self.<attr2> = <param2>
        .
        .
        .
        # As many attributes as needed

   def <method_name>(self, <param1>, ...):
       <code>

   # As many methods as needed

Tip: self refers to an instance of the class (an object created with the class blueprint).

Different elements of class.


Class Header -> name of the class  
    
    class Dog:
    
    If the class inherits attributes and methods from another class, 
    we will see the name of the class within parentheses

    class Poodle(Dog):
    
    In Python, we write class name in Upper Camel Case (also known as Pascal Case), 
    in which each word starts with an uppercase letter. For example: FamilyMember
'''

class Dog:
    pass

#### Insatnces & Instance Attributes ####

'''
__init__ and instance attributes

    We are going to use the class to create object in Python, just like we build real houses 
    from blueprints.

    The objects will have attributes that we define in the class. Usually, we initialize these 
    attributes in __init__. This is a method that runs when we create an instance of the class.

    This is the general syntax:

    def __init__(self, <parameter1>, <parameter2>, ...):
            self.<attribute1> = <parameter1>  # Instance attribute
            self.<attribute2> = <parameter2>  # Instance attribute
            .
            .
            .
            # As many instance attributes as needed

'''

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# creating instance

my_dog = Dog("Nora", 10)


# Some classes won't require any arguments to create an instance - just write empty parentheses.

class Circle:

    def __init__(self):
        self.radius = 1

#To create an instance:

my_circle = Circle()

'''
Default Arguments

We can also assign default values for the attributes and give the option to the user 
if they would like to customize the value.

In this case, we would write <attribute>=<value> in the list of parameters.
'''

# This is an example:

class Circle:

    def __init__(self, radius=1):
        self.radius = radius

# Now we can create a Circle instance with the default value for the radius by 
# omitting the value or customize it by passing a value.

'''
To access an instance attribute, we use this syntax:

<object_variable>.<attribute>
'''

print(my_dog.name)


'''
To update an instance attribute, we use this syntax:

<object_variable>.<attribute> = <new_value>
'''

my_dog.name = "Norita"
print(my_dog.name)


'''
To remove an instance attribute, we use this syntax:

del <object_variable>.<attribute>
'''

del my_dog.name

try:
    print(my_dog.name)
except:
    print('this attribute does not exist')    

# Similarly, we can delete an instance using del

del my_dog


'''
Public vs. Non-Public Attributes in Python

In Python, we don't have access modifiers to functionally restrict access to the instance 
attributes, so we rely on naming conventions to specify this.

For example, by adding a leading underscore, we can signal to other developers that an 
attribute is meant to be non-public.

For example:

class Dog:

    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age   # Non-Public attribute

The Python documentation mentions:

Use one leading underscore only for non-public methods and instance variables.

Always decide whether a class's methods and instance variables (collectively: "attributes") 
should be public or non-public. If in doubt, choose non-public; it's easier to make it public 
later than to make a public attribute non-public.

Non-public attributes are those that are not intended to be used by third parties; 
you make no guarantees that non-public attributes won't change or even be removed. - source

However, as the documentation also mentions:

We don't use the term "private" here, since no attribute is really private in Python 
(without a generally unnecessary amount of work). - source

Technically, we can still access and modify the attribute if we add the leading underscore 
to its name, but we shouldn't.
'''


#### Class Attributes ####

'''
Class attributes are shared by all instances of the class. 
They all have access to this attribute and they will also be affected by any changes 
made to these attributes.
'''

class Dog:

    # Class attributes
    kingdom = "Animalia"
    species = "Canis lupus"

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Usually, they are written before the __init__ method

'''
To update a class attribute, we use this syntax:

<class_name>.<attribute> = <value>
'''

print(Dog.kingdom)

# We use del to delete a class attribute

del Dog.kingdom


'''
Methods

Methods represent the functionality of the instances of the class.

Instance methods can work with the attributes of the instance that is calling the method 
if we write self.<attribute> in the method definition.

This is the basic syntax of a method in a class. 
They are usually located below __init__:

class <ClassName>:

    # Class attributes

    # __init__

    def <method_name>(self, <param1>, ...):
        <code>

--> Instance methods must always have self as the first parameter.
'''

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"woof-woof. I'm {self.name}")

# Syntax to call this instance method - <object_variable>.<method>(<arguments>)

my_dog = Dog("Nora", 10)
my_dog.bark()

# Here we have a Player class with an increment_speed method with one parameter:

class Player:

    def __init__(self, name):
        self.name = name
        self.speed = 50

    def increment_speed(self, value):
        self.speed += value

my_player = Player("Nora")

print(my_player.speed)

my_player.increment_speed(5)

print(my_player.speed)


'''
Properties, Getters and Setters in Python

Getters and setters are methods that we can define to get and set the value of an instance 
attribute, respectively. They work as intermediaries to "protect" the attributes from direct 
changes.

In Python, we typically use properties instead of getters and setters. Let's see how we can 
use them.

To define a property, we write a method with this syntax:

@property
def <property_name>(self):
    return self.<attribute>

This method will act as a getter, so it will be called when we try to access the value of 
the attribute.

Now, we may also want to define a setter:

@<property_name>.setter
def <property_name>(self, <param>):
    self.<attribute> = <param>

And a deleter to delete the attribute:

@<property_name>.deleter
def <property_name>(self):
    del self.<attribute>

Tip: you can write any code that you need in these methods to get, set, and delete an attribute. It is recommended to keep them as simple as possible.

'''

class Dog:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name


