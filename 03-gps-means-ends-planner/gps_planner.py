def gps(initial_states, goal_states, operators):
   prefix = 'EXECUTING '
   for operator in operators:
      operator['action'] = operator['action'].upper()
      #print("Test before\n", operator['add'])
      operator['add'].append(prefix + operator['action'])
      #print("Test\n",operator['add'])
      operator['preconds'] = [pre.upper() for pre in operator['preconds']]
      operator['delete'] = [dlst.upper() for dlst in operator['delete']]
      operator['add'] = [add.upper() for add in operator['add']]
      #print(operator['add'])
   initial_states =  [state.upper() for state in initial_states]
   goal_states = [goal.upper() for goal in goal_states]

   final_states = achieve_all(initial_states, operators, goal_states, [])
   if not final_states:
      return None
   actions = [state for state in final_states if state.startswith(prefix)]
   for a in actions:
      print(a)
   return actions
def achieve_all(states, ops, goals, goal_stack):
   for goal in goals: # ['son at school']
      states = achieve(states, ops, goal, goal_stack)
      if not states:
         return None
   for goal in goals:
      if goal not in states:
         return None
   return states
def achieve(states, operators, goal, goal_stack):
   #print(len(goal_stack), 'Achieving: %s' % goal)
   if goal in states:
      #print(len(goal_stack), 'Achieved: %s' % goal)
      return states
   if goal in goal_stack:
      return None
   for op in operators:
      if goal not in op['add']:
         continue
      result = apply_operator(op, states, operators, goal, goal_stack)
      if result:
         return result
def apply_operator(operator, states, ops, goal, goal_stack):
   #print(len(goal_stack), 'Consider: %s' % operator['action'])
   result = achieve_all(states, ops, operator['preconds'], [goal] + goal_stack)
   if not result:
      return None
   #print(len(goal_stack), 'Action: %s' % operator['action'], '  Achieved: %s' % goal)
   add_list, delete_list = operator['add'], operator['delete']
   #print(operator['action'])
   return [state for state in result if state not in delete_list] + add_list

sch_ops = [
   {
       "action": "drive son to school",
       "preconds": ["son at home", "car works"],
       "add": ["son at school"],
       "delete": ["son at home"]
   },
   {   "action": "shop installs battery",
       "preconds": ["car needs battery", "shop knows problem", "shop has money"],
       "add": ["car works"],
       "delete": []
   },
   {   "action": "tell shop problem",
       "preconds": ["in communication with shop"],
       "add": ["shop knows problem"],
       "delete": []
   },
   {   "action": "telephone shop",
       "preconds": ["know phone number"],
       "add": ["in communication with shop"],
       "delete": []
   },
   {   "action": "look up number",
       "preconds": ["have phone book"],
       "add": ["know phone number"],
       "delete": []
   },
   {   "action": "give shop money",
       "preconds": ["have money"],
       "add": ["shop has money"],
       "delete": ["have money"]
   }
    ]
block_ops = [
{"action":"Move block C on table",
   "preconds":["Block C on A", "C-free"],
   "add":["Block C on table", "A-free"],
   "delete":["Block C on A"]},
{"action":"Move block A on table",
   "preconds":["Block A on B","A-free"],
   "add":["Block A on table", "B-free"],
   "delete":["Block A on B"]},
{"action":"Move block B on C",
   "preconds":["Block B on table", "B-free", "C-free"],
   "add":["Block B on C"],
   "delete":["Block B on table","C-free"]},
{"action":"Move block A on B",
   "preconds":["Block A on table", "A-free","B-free"],
   "add":["Block A on B"],
   "delete":["Block A on table", "B-free"]}
]
# Preparing a Sandwich
sandwich_ops = [
    {
        "action": "spread cheese on bread",
        "preconds": ["bread available", "cheese available", "knife clean"],
        "add": ["cheese spread"],
        "delete": ["cheese available", "knife clean"]
    },
    {
        "action": "place bread on plate",
        "preconds": ["bread available", "plate clean"],
        "add": ["bread placed"],
        "delete": ["plate clean"]
    },
    {
        "action": "assemble sandwich",
        "preconds": ["cheese spread", "bread placed"],
        "add": ["sandwich ready"],
        "delete": ["cheese spread", "bread placed"]
    },
]
# Cleaning a Room
cleaning_ops = [
    {
        "action": "pick up trash",
        "preconds": ["trash on floor"],
        "add": ["trash removed"],
        "delete": ["trash on floor"]
    },
    {
        "action": "wipe table",
        "preconds": ["dirty table"],
        "add": ["table clean"],
        "delete": ["dirty table"]
    },
    {
        "action": "wash dishes",
        "preconds": ["unwashed dishes"],
        "add": ["dishes clean"],
        "delete": ["unwashed dishes"]
    },
    {
        "action": "final cleanup",
        "preconds": ["trash removed", "table clean", "dishes clean"],
        "add": ["room clean"],
        "delete": ["trash removed", "table clean", "dishes clean"]
    },
]
# Preparing Coffee
coffee_ops = [
    {
        "action": "boil water",
        "preconds": ["water available"],
        "add": ["hot water"],
        "delete": ["water available"]
    },
    {
        "action": "add coffee powder",
        "preconds": ["coffee powder available", "clean mug"],
        "add": ["coffee in mug"],
        "delete": ["coffee powder available"]
    },
    {
        "action": "pour water into mug",
        "preconds": ["hot water", "coffee in mug"],
        "add": ["coffee ready"],
        "delete": ["hot water", "coffee in mug"]
    },
]
# Driving to Work
drive_ops = [
    {
        "action": "start car",
        "preconds": ["car at home", "key available"],
        "add": ["car started"],
        "delete": ["key available"]
    },
    {
        "action": "drive to work",
        "preconds": ["car started", "enough fuel"],
        "add": ["at work"],
        "delete": ["car at home", "car started"]
    },
]
# Building a House
build_ops = [
    {
        "action": "build walls",
        "preconds": ["foundation ready", "bricks available", "cement available"],
        "add": ["walls built"],
        "delete": ["bricks available", "cement available"]
    },
    {
        "action": "add roof",
        "preconds": ["walls built"],
        "add": ["house built"],
        "delete": ["walls built"]
    },
]
# Shopping for Groceries
shopping_ops = [
    {
        "action": "go to store",
        "preconds": ["at home", "list ready", "have car"],
        "add": ["at store"],
        "delete": ["at home"]
    },
    {
        "action": "buy groceries",
        "preconds": ["at store", "have money"],
        "add": ["groceries bought"],
        "delete": ["have money"]
    },
    {
        "action": "return home",
        "preconds": ["groceries bought"],
        "add": ["at home"],
        "delete": ["at store"]
    },
]
cooking_ops = [
    {
        "action": "go to kitchen",
        "preconds": ["at home"],
        "add": ["in kitchen"],
        "delete": ["at home"]
    },
    {
        "action": "prepare ingredients",
        "preconds": ["in kitchen", "have groceries"],
        "add": ["ingredients ready"],
        "delete": []
    },
    {
        "action": "cook meal",
        "preconds": ["ingredients ready", "stove working"],
        "add": ["dinner cooked"],
        "delete": ["ingredients ready"]
    },
    {
        "action": "serve meal",
        "preconds": ["dinner cooked"],
        "add": ["dinner served"],
        "delete": ["dinner cooked"]
    },
]

gps(["Block B on table", "Block A on B", "Block C on A", "C-free"],
["Block C on table", "Block B on C", "Block A on B", "A-free"] ,block_ops )





def printline(arg):
    print("\n",arg,"Example\n__________________________\n")
printline("House ")
gps(["foundation ready", "bricks available", "cement available"],
    ["house built"],
    build_ops
)
printline("Work ")
gps(["car at home", "enough fuel", "key available"],
    ["at work"],
    drive_ops
)
printline("Coffee ")
gps(["water available", "coffee powder available", "clean mug"],
    ["coffee ready"],
    coffee_ops
)
printline("Cleaning ")
gps(["trash on floor", "dirty table", "unwashed dishes"],
    ["room clean"],
    cleaning_ops
)
printline("Sandwitch ")
gps(["bread available", "cheese available", "knife clean", "plate clean"],
    ["sandwich ready"],
    sandwich_ops
)
printline("Grocery ")
gps (["At home", "Grocery list ready", "Have money", "Have car"], ["groceries bought", "At home"], shopping_ops
)
printline("Drive son to School ")


gps(
    ["at home", "have groceries", "stove working"],
    ["dinner served", "at home"],
    cooking_ops
)

gps_operators = [
    {
        'action': 'turn-off-tv',
        'preconds': ['watching-tv', 'Tv-on'],
        'add': ['Tv-off'],
        'delete': ['watching-tv', 'Tv-on']
    },
    {
        'action': 'open-door',
        'preconds': ['outside-bedroom'],
        'add': ['door-open'],
        'delete': []
    },
    {
        'action': 'step-inside',
        'preconds': ['outside-bedroom', 'door-open'],
        'add': ['inside-bedroom'],
        'delete': ['outside-bedroom']
    },
    {
        'action': 'rest',
        'preconds': ['inside-bedroom', 'Tv-off'],
        'add': ['resting'],
        'delete': []
    }
]
# Call for - Drive son to school
gps(["son at home", "have money", "have phone book", "car needs battery"],
    ["son at school"], sch_ops)
