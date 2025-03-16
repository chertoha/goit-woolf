from linked_list import LinkedList, Node


class ExtendedLinkedList(LinkedList):
    def reverse(self):
        current, prev = self.head, None
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def _sorted_insert(self, head: Node | None, new_node: Node) -> Node:
        if head is None or (new_node.data is not None and head.data is not None and new_node.data < head.data):
            new_node.next = head
            return new_node

        current = head
        while current.next and current.next.data is not None and new_node.data is not None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return head

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    dummy = Node()
    tail = dummy

    head1, head2 = list1.head, list2.head

    while head1 is not None and head2 is not None:
        if head1.data is not None and head2.data is not None and head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 if head1 is not None else head2

    merged_list = LinkedList()
    merged_list.head = dummy.next

    return merged_list

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


l1 = ExtendedLinkedList()
l1.insert_at_end(1)
l1.insert_at_end(2)
l1.insert_at_end(3)
l1.insert_at_end(4)
print("До реверсу:")
l1.print_list()
l1.reverse()
print("Після реверсу:")
l1.print_list()

print("----------------------------------------------------")
print("----------------------------------------------------")

l2 = ExtendedLinkedList()
l2.insert_at_end(4)
l2.insert_at_end(2)
l2.insert_at_end(1)
l2.insert_at_end(3)

print("До сортування:")
l2.print_list()

l2.insertion_sort()

print("Після сортування:")
l2.print_list()

print("----------------------------------------------------")
print("----------------------------------------------------")

l3 = LinkedList()
l3.insert_at_end(1)
l3.insert_at_end(3)
l3.insert_at_end(5)

l4 = LinkedList()
l4.insert_at_end(2)
l4.insert_at_end(4)
l4.insert_at_end(6)

print("Перший список:")
l3.print_list()

print("Другий список:")
l4.print_list()

merged = merge_sorted_lists(l3, l4)

print("Об'єднаний відсортований список:")
merged.print_list()
