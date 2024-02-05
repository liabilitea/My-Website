# Define a Node class to represent a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to merge two sorted linked lists
def merge_sorted_lists(list1, list2):
    merged_list = Node(None)  # Start with a node containing None
    current_node = merged_list

    while list1 is not None and list2 is not None:
        if list1.data is not None and (list2.data is None or list1.data <= list2.data):
            current_node.next = Node(list1.data)
            list1 = list1.next
        else:
            current_node.next = Node(list2.data)
            list2 = list2.next
        current_node = current_node.next

    # If one list is not fully traversed, append the remaining nodes
    while list1 is not None:
        current_node.next = Node(list1.data)
        list1 = list1.next
        current_node = current_node.next

    while list2 is not None:
        current_node.next = Node(list2.data)
        list2 = list2.next
        current_node = current_node.next

    return merged_list.next

# Function to print the elements of a linked list
def print_linked_list(head):
    elements = []
    current_node = head
    while current_node is not None:
        elements.append(str(current_node.data))
        current_node = current_node.next
    elements.append("None")
    return " -> ".join(elements)

# Function to create a linked list based on user input
def create_linked_list(size, values):
    head = None
    try:
        if size != len(values):
            raise ValueError("Size should be equal to the number of values.")

        # Validate values as floats or integers and ensure they are within the range -100 to 100
        values = [val.strip() for val in values]
        numeric_values = []
        
        for val in values:
            try:
                numeric_val = float(val) if '.' in val else int(val)
                if not (-100 <= numeric_val <= 100):
                    raise ValueError("Values should be in the range from -100 to 100.")
                numeric_values.append(numeric_val)
            except ValueError:
                raise ValueError(f"Invalid value '{val}'.")

        for data in numeric_values:
            new_node = Node(data)
            if head is None:
                head = new_node
            else:
                current_node = head
                while current_node.next is not None:
                    current_node = current_node.next
                current_node.next = new_node
    except ValueError as e:
        raise ValueError(f"{e} Please enter valid numeric value.")

    return head