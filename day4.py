class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        new_start = head.next.next
        first = head
        second = head.next
        second.next = first
        first.next = self.swapPairs(new_start)
        return second
def printList(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" -> ".join(elements) if elements else "Empty List")
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
print("Original list:")
printList(head)
head = head.swapPairs(head)
print("After swapping pairs:")
printList(head)
