############################## Task 01      ########################################################################

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        if len(self.scores) == 0:
            return 0
        average = sum(self.scores) / len(self.scores)
        return float(average)

    def get_grade(self):
        if len(self.scores) == 0:
            return "No grades"

        average = self.get_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        else:
            return "F"

    def display_info(self):
        print("Student Name:", self.name)
        print("Scores:", self.scores)
        print("Average Score: {:.1f}".format(self.get_average()))
        print("Grade:", self.get_grade())


student1 = Student("Ali")
student1.add_score(85)
student1.add_score(92)
student1.add_score(78)

student1.display_info()

############################## Task 02     #######################################################################

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        if name not in self.contacts:
            self.contacts[name] = number
            print("Contact '" + name + "' added successfully!")
        else:
            existing_number = self.contacts[name]
            answer = input("Contact '" + name + "' already exists with number: " + existing_number + ". Overwrite? (y/n): ")

            if answer.lower() == "y":
                self.contacts[name] = number
                print("Contact '" + name + "' updated successfully!")
            elif answer.lower() == "n":
                print("Contact '" + name + "' was not changed.")

    def find_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "Contact not found"

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return "Contact deleted"
        else:
            return "Contact not found"

    def list_all_contacts(self):
        if len(self.contacts) == 0:
            print("Phonebook is empty")
        else:
            for name in self.contacts:
                print(name + ": " + self.contacts[name])

    def count_contacts(self):
        return len(self.contacts)


book = PhoneBook()
book.add_contact("Ali", "03001234567")
book.add_contact("Sara", "03111234567")

print(book.find_contact("Ali"))
print(book.find_contact("Ahmed"))

book.list_all_contacts()
print("Total contacts:", book.count_contacts())

print(book.delete_contact("Sara"))
book.list_all_contacts()

##################################      Task 03        #########################################################

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price):
        item = (item_name, price)
        self.items.append(item)
        print("Added " + item_name + " to cart")

    def remove_item(self, item_name):
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                del self.items[i]
                return "Item removed"
        return "Item not found"

    def calculate_total(self):
        total = 0
        for item in self.items:
            total = total + item[1]
        return float(total)

    def show_cart(self):
        if len(self.items) == 0:
            print("Your cart is empty")
        else:
            index = 1
            for item in self.items:
                print(str(index) + ". " + item[0] + ": $" + "{:.2f}".format(item[1]))
                index = index + 1

    def get_item_count(self):
        return len(self.items)

    def clear_cart(self):
        self.items = []
        print("Cart cleared successfully!")


cart = ShoppingCart()
cart.add_item("Shirt", 25.50)
cart.add_item("Shoes", 60.00)
cart.add_item("Shirt", 25.50)

cart.show_cart()
print("Total:", cart.calculate_total())
print("Item Count:", cart.get_item_count())

print(cart.remove_item("Shirt"))
cart.show_cart()

cart.clear_cart()
cart.show_cart()

##################################      Task 04        #########################################################

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_counter = 0

    def add_task(self, task_name, priority=2):
        self.task_counter = self.task_counter + 1

        new_task = {
            "id": self.task_counter,
            "task": task_name,
            "priority": priority,
            "completed": False
        }

        self.tasks.append(new_task)
        print("Task added: " + task_name + " (Priority: " + str(priority) + ")")

    def view_all_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found")
        else:
            for task in self.tasks:
                if task["completed"] == True:
                    status = "Completed"
                else:
                    status = "Pending"

                print("ID: " + str(task["id"]) + " | Task: " + task["task"] + " | Priority: " + str(task["priority"]) + " | Status: " + status)

    def view_completed_tasks(self):
        completed_tasks = []

        for task in self.tasks:
            if task["completed"] == True:
                completed_tasks.append(task)

        if len(completed_tasks) == 0:
            print("No completed tasks")
        else:
            for task in completed_tasks:
                print("ID: " + str(task["id"]) + " | Task: " + task["task"] + " | Priority: " + str(task["priority"]) + " | Status: Completed")

    def view_pending_tasks(self):
        pending_tasks = []

        for task in self.tasks:
            if task["completed"] == False:
                pending_tasks.append(task)

        if len(pending_tasks) == 0:
            print("No pending tasks")
        else:
            for task in pending_tasks:
                print("ID: " + str(task["id"]) + " | Task: " + task["task"] + " | Priority: " + str(task["priority"]) + " | Status: Pending")

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return "Task completed"

        return "Task not found"

    def get_high_priority_tasks(self):
        high_priority_names = []

        for task in self.tasks:
            if task["priority"] == 1 and task["completed"] == False:
                high_priority_names.append(task["task"])

        return high_priority_names

    def delete_task(self, task_id):
        for i in range(len(self.tasks)):
            if self.tasks[i]["id"] == task_id:
                del self.tasks[i]
                return "Task deleted"

        return "Task not found"


manager = TaskManager()
manager.add_task("Finish assignment", 1)
manager.add_task("Buy groceries")
manager.add_task("Clean room", 3)

manager.view_all_tasks()

print(manager.mark_completed(2))

manager.view_completed_tasks()
manager.view_pending_tasks()

print("High priority pending tasks:", manager.get_high_priority_tasks())

print(manager.delete_task(3))
manager.view_all_tasks()
