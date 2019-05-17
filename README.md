# PR301-Assignment-2

## Bad Smell documentation

### Smell detection

Notes: 
1. From commit 2 (where the comment is in the repository) of the refactoring history of fileProcessor.py, ignore this and all future commits made after this one on fileProcessor.py. These are incorrect due to the mistake discussed last Friday. 
2. The third bad smell refactoring is done under "patch-1" branch.

#### Name: Large Class

Location:
PR301-Assignment-1-Version-1-fileHandler.py-PrintClass-between Line 6 and 184

Reasons:

1.	This class contains many fields. This is a key sign of a large class. 
2.	This class contains far too many methods, but importantly, these methods can easily be grouped into three types: methods for inputting data, methods for processing data, and methods for outputting data to files. This indicates that this class handles multiple groups of responsibilities, which shouldn’t be the case. A class should only handle one group of responsibilities.
3.	This is a very large class. 178 lines of code. 
4.	The class is going to be hard to read and understand because there are many methods doing too many things, so as a result it will be hard to add functionality to the class.

Strategies/Approaches:

Move method, move attribute, replace class with multiple classes via composition. 
1.	I will first remove any unnecessary code, for example calls to attributes or methods which, when removed, does not affect the external behaviour of the class. This will ensure that when refactoring, they will not cause any extra complications. 
2.	I will then consider the total methods in these classes as well as its attributes. Then, I will group methods with similar functions. I will group attributes according to the methods using them. Then, I will create two new classes (since this class does 3 groups of things), give them appropriate names for what they do, and then assign the appropriate methods and attributes to them. 
3.	I will execute move method for each method that is moved to the two other classes. I will do so one method by one method, and not shift more than one method at the same time and test after each move, to ensure that my tests still pass, and the code wasn’t broken by the move method. Each time I want to commit to the repository I test the code first to ensure it is working.
4.	If a class needs to use methods/attributes from another class, I will declare an object of the class with the desired methods/attributes in the class which needs to use the methods and then use that object to access its methods/attributes. This is important for ensuring that the external behaviour of fileHandler does not change. 
5.	I will continue until each class has its own appropriate methods and attributes, and the responsibility of the original class is split between these three classes. 

#### Name: Long Method

Location: 
PR301-Assignment-1-Version-1-fileHandler.py-PrintClass-output_class-between Line 128 and 167 

Reasons: 

1.	As a rule of thumb, any method which is longer than ten lines should be scrutinized. 
2.	Since the output_class method is 39 lines long, it fulfils one of the conditions for the long method bad smell.
3.	The other is that a method should only perform one task. Looking at the output_class method, it performs numerous tasks, including validating data, appending class data to form a string and exception handling. Ideally all these tasks be split into their own separate methods, and since the method is doing far more tasks than one, this qualifies it as having the long method bad smell. This also makes the method really hard to read and complicated to understand.

Strategies/approaches:

I choose Extract Method for refactoring this long method, because since it performs more than one function, separate functions and has blocks of code which can be grouped together can be extracted from it, each fulfilling a separate task. Hence, this will delegate responsibility to other methods, instead of having all the responsibility on this method and making it so long and cumbersome. 

Extract method

Steps:

1.	I will first begin by replacing all references to local variables in the output_class method, which contain the results of method calls, with the actual calls to the methods. This way, local variables will not cause complications with method extraction. 
2.	Then, I will create new methods, each performing one task that the original method performed. 
3.	Then, I will extract the grouped code related to each task and paste it into the body of each new method.
4.	I will then delete the original code which was pasted into each new method and replace each instance of it with calls to its corresponding new method.
5.	Due to the fact that certain code groups which perform a particular task in the original output_class method encapsulate other code groups which perform a different task, the extract method will need to be repeated iteratively in steps for that particular situation, because applying extract method on the outer code group will not completely get rid of the bad smell, since the resulting new method will still perform more than one task due to a code group within it performing an extra task, causing it to perform more than one task and cause the bad smell to still remain. I will carry out this process as follows:
a.	Extract out the largest code blocks which do one thing out of the original output_class method. Smaller code groups inside it which perform different tasks are ignored for now.
b.	Test the code to ensure it is still working correctly.
c.	Extract the smaller code group inside the new method created by previously extracting the largest code block out of the original method. 
d.	Test the code to ensure it is still working correctly. 
e.	Repeat until all levels of nested functionality are removed (and thus the bad smell will then be totally gone). 
Switch Statements

#### Name: Switch statements

Location: 
PR301-Assignment-1-Version-1-command.py-Command-do_display-between Line 45 and 50

Reasons:

1.	The use of if…elif…elif statement is the main sign of this bad smell. 
2.	This is a problem because upon adding a new condition, every section of code containing switch statements will need to be changed. 
3.	The bad smell appears in the form that the same option is compared every time, introducing some repetition in the code, and thus reducing its quality, understandability and reusability. 
4.	Furthermore, the method is trying to do many things at once, checking for various relationships in the input. 
5.	Also it is comparing the “option” and making sure it is equal to different strings. This confirms it is the switch statement bad smell.
6.	The above reasons make the method complicated and hard to read and understand. It will be hard to modify or add onto any of this code as a result.

Strategies/approaches:

Replace repeated if statement with dictionary.
I will replace the if statements with a dictionary and a single if statement, to eliminate the repetition of if statement conditions. The values the option is being checked against will become the keys of the dictionary, and the methods to be run will become the values of the dictionary. Explained in detail below:

Steps:

1.	I will create a python dictionary with the appropriate name and use it to store the keys corresponding to the options in the repeated if statements and the values corresponding to the lines of code to be run for each option value.
2.	Then, I will rewrite the code such that it checks the input option against the keys of the dictionary created in the previous step, if it matches one, then its corresponding value which is a method will then be run, if not then it will not be run. 

### Refactoring

#### Identification of worst smell(s)

The worst bad smell is Large Class. It is the worst smell because the total amount of code this bad smell affects (178 lines) is the most compared to the other bad smells found. Documented in the table below is a summary of the number of lines of code in total affected by each bad smell, arranged in descending order which helped guide my decision on which bad smell was the worst. The worst bad smell was removed first, followed by the second worst, and the third worst. 

#### Effectiveness Evaluations

Large Class

The bad smell was removed, and now the classes each have their own purpose, and deal with one group of functions each correctly. It is also easier to understand and read the code now. Therefore, we can conclude that the bad smell has successfully been removed. However, I did bring a new bad smell, inappropriate intimacy into the program since the new methods in fileHandler which need to be there since the external behaviour of fileHandler cannot change use the methods of the other two classes, but since this only amounts to 16 lines of code, which is fewer lines than the next worst bad smell has (39 lines), I will be refactoring the next worst bad smell which is long method instead of this one. The software quality has now improved significantly via the removal of much complication and confusion by having each class do its separate group of functions. 

Long Method

The bad smell was indeed removed, and responsibilities of the output_class method were distributed to the appropriately named methods. It is now clearer and easier to understand, and therefore code quality has improved, since work is split between these methods so that output_class does not have to do all the work the other methods are doing itself. By doing so, I have increased readability and its now easier to add functional code. Also, the parts of output_class which included exception handling and validation of class names, attribute names, and method names have not been shifted to their own methods, so as not to confuse the purpose of output_class. These exception handling and validating methods are now called by the handler for each aspect of the output_class method, (i.e. add_class_names, add_methods, add_attributes) as they should be, since these methods should handle classes, methods, and attributes and therefore it is their responsibility to check the validity of what they are handling. No foreseeable bad smells were added by refactoring this, so I deem the refactoring process successful. Therefore, I then refactored the next worst bad smell, which was switch statements.  

Switch Statements

The bad smell has been removed. The dictionary helped to eliminate the repetition of if bad smell, and makes the code easier to read and understand, as well as slightly shorter. Therefore, the code is now easier to read. No new bad smells have been introduced by this refactoring. The quality of the code has improved because it is now more modular and able to be customized, understood and read more easily. 
