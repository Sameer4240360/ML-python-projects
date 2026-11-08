####################     QUESTION NO 01        ####################
def analyze_scores(scores):
    highest = max(scores)
    lowest = min(scores)
    average = round(sum(scores) / len(scores), 2)
    passed = 0
    failed = 0

    for score in scores:
        if score >= 50:
            passed += 1
        else:
            failed += 1

    result = {
        "highest": highest,
        "lowest": lowest,
        "average": average,
        "passed": passed,
        "failed": failed
    }
    return result

scores = [45, 67, 89, 32, 90, 55, 40]
print(analyze_scores(scores))

####################     QUESTION NO 02        ####################
def find_free_courses(enrollments, all_courses):
    enrolled_courses = set()

    for student in enrollments:
        for course in enrollments[student]:
            enrolled_courses.add(course)

    all_courses_set = set(all_courses)
    free_courses = all_courses_set - enrolled_courses

    return free_courses


all_courses = ("CS101", "CS102", "MTH101", "PHY101", "ENG101")

enrollments = {
    "Ali": ("CS101", "MTH101"),
    "Sara": ("CS102",),
    "Ahmed": ("CS101", "PHY101")
}

print(find_free_courses(enrollments, all_courses))

####################     QUESTION NO 03        ####################

def add_contact(phonebook, name, number):
    phonebook[name] = number
    print(name, " added")


def search_contact(phonebook, name):
    if name in phonebook:
        print(name, " number is:", phonebook[name])
    else:
        print(name, "not found")


def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(name, "deleted from the phonebook.")
    else:
        print(name, "not found")

phonebook = {}

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(phonebook, name, number)
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(phonebook, name)
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(phonebook, name)
    elif choice == "4":
        break
    else:
        print("Invalid choice:")

####################     QUESTION NO 04        ####################
def manage_library(books, borrowed):
    avail = set()
    full = []
    wait = {}
    sugg = []

    for bid, title, copies in books:
        b_list = borrowed.get(bid, [])
        count = len(b_list)

        if count < copies:
            avail.add(title)
        else:
            full.append(title)

        if count > copies:
            wait[title] = b_list[copies:]
            sugg.append(title)

    report = {
        "available": avail,
        "fully_borrowed": full,
        "waiting_lists": wait,
        "suggestions": sugg
    }

    return report


books = [
    ("B001", "Python Basics", 2),
    ("B002", "Data Structures", 1),
    ("B003", "AI for Beginners", 3),
]

borrowed = {
    "B001": ["Ali", "Sara", "Ahmed"],
    "B002": ["Hassan"],
    "B003": ["Bilal"],
}

report = manage_library(books, borrowed)
print(report)
