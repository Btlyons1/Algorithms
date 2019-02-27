from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]# an array of all your neighbors
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny", "mango"]
graph["anuj"] = [] # direct graph - one way relationship
graph["peggy"] = []
graph["thom"] = []
graph["mango"] = []
graph["jonny"] = []


# Simple implementation of a queue to search for a mango seller.
# For simplicity, a mango seller is a person whose name starts with m
def search(name):
    print(name)
    search_queue = deque() # creates a new queue
    search_queue += graph # Adds your neighbors to the search queue
    searched = [] # keep track of everyone you've already searched
    while search_queue:
        person = search_queue.popleft() # grabs first person off the queue
        if person_is_seller(person):
            print(person + " is a mango seller")
            return True
        else:
            search_queue += graph[person] #add the persons network to the queue
            searched.append(person) #add person to to
    return False # no one in the queue was a mango seller

def person_is_seller(name):
    # if person name starts with m they're a seller
    return name[0].lower() == 'm'

search(graph)