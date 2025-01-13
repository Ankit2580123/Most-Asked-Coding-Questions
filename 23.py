#implement Simple Linked List and traverse it

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head as None

    # Method to append data to the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:     # If the list is empty, make the new node the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Link the new node at the end

    
    
    def traverse(self):
        current=self.head
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print("None")
    
# Function to take inputs for a linked list
def create_linked_list():
        ll = LinkedList()
        print("Enter elements of the linked list (type 'done' to finish):")
        while True:
            user_input = input("Enter a number: ")
            if user_input.lower() == 'done':  # Exit loop when 'done' is entered
                break
            try:
                ll.append(int(user_input))  # Convert input to integer and append
            except ValueError:
                print("Please enter a valid integer.")
        return ll

# Example usage
linked_list = create_linked_list()
print("The linked list is:")
linked_list.traverse()
    


