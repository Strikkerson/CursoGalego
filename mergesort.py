class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(l1, l2):
    head = Node()
    tail = head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    tail.next = l1 if l1 else l2

    return head.next


def mergesort(head):
    if not head or not head.next:
        return head

    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None

    l1 = mergesort(head)
    l2 = mergesort(after_middle)

    sorted_list = merge(l1, l2)

    return sorted_list

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


values = [34, 7, 23, 32, 5, 62, 14, 78, 9, 41]

# Initialize the head of the list
head = Node(values[0])
current = head

# Build the rest of the linked list
for val in values[1:]:
    current.next = Node(val)
    current = current.next

print("Unsorted")
print_linked_list(head)

print("Sorted")
print_linked_list(mergesort(head))



