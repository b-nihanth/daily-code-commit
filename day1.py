# Simple Calculator(Addition,Subtraction,Multiplication,Division)
def calculator():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Choose (+, -, *, /) or 'exit' to quit: ").strip()
            
            if operation == 'exit':
                break
            elif operation == '+':
                print(f"Result: {num1 + num2}\n")
            elif operation == '-':
                print(f"Result: {num1 - num2}\n")
            elif operation == '*':
                print(f"Result: {num1 * num2}\n")
            elif operation == '/':
                print(f"Result: {num1 / num2}\n" if num2 != 0 else "Cannot divide by zero!\n")
            else:
                print("Invalid operation!\n")
        except ValueError:
            print("Invalid input! Please enter numbers.\n")

calculator()


#To-Do List Manager(File Handling)
def todo_list():
    print("To-Do List Manager")
    tasks = []
    while True:
        action = input("Add task (A), View tasks (V), Remove task (R), Exit (E): ").strip().upper()
        
        if action == 'A':
            task = input("Enter task: ")
            tasks.append(task)
            with open("todo.txt", "a") as file:
                file.write(task + "\n")
            print("Task added!\n")
        
        elif action == 'V':
            print("\nCurrent To-Do List:")
            with open("todo.txt", "r") as file:
                print(file.read())

        elif action == 'R':
            task_to_remove = input("Enter task to remove: ")
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                with open("todo.txt", "w") as file:
                    for task in tasks:
                        file.write(task + "\n")
                print("Task removed!\n")
            else:
                print("Task not found!\n")
        
        elif action == 'E':
            break
        else:
            print("Invalid option!\n")

todo_list()


#Random Password Generator
import random
import string

def password_generator(length=12):
    print("Random Password Generator")
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated Password: {password}\n")

password_generator()


#Palindrome Checker
def is_palindrome(word):
    return word == word[::-1]

print("Palindrome Checker")
word = input("Enter a word: ").strip().lower()
if is_palindrome(word):
    print(f"{word} is a palindrome!\n")
else:
    print(f"{word} is NOT a palindrome!\n")


#Student Grade Management(OOP)
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    
    def average(self):
        return sum(self.scores) / len(self.scores)

students = [
    Student("Alice", [85, 90, 88]),
    Student("Bob", [78, 85, 82]),
    Student("Charlie", [92, 95, 96])
]

print("Student Grade Management")
for student in students:
    print(f"{student.name}: Average Score = {student.average():.2f}")

#Prime Number Finder
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\nPrime Number Finder")
n = int(input("Enter a number to check if it's prime: "))
print(f"{n} is Prime!" if is_prime(n) else f"{n} is NOT Prime!")


#Simple Banking System(OOP & File Handling)
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!\n")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining Balance: ${self.balance}\n")

    def save_to_file(self):
        with open(f"{self.name}_account.txt", "w") as file:
            file.write(f"Account Holder: {self.name}\nBalance: ${self.balance}\n")

print("\nSimple Banking System")
name = input("Enter account holder name: ")
account = BankAccount(name, 1000)

while True:
    action = input("Deposit (D), Withdraw (W), View Balance (V), Exit (E): ").strip().upper()
    
    if action == 'D':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        account.save_to_file()
    
    elif action == 'W':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        account.save_to_file()
    
    elif action == 'V':
        print(f"Current Balance: ${account.balance}\n")
    
    elif action == 'E':
        print("Exiting Banking System.\n")
        break
    
    else:
        print("Invalid action!\n")
 
