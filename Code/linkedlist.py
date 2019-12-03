#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())
    
    def __iter__(self):
        """Returns an interable representation of this linked list"""
        return iter([value for value in self.items()])

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?
        Running time: O(n) since it goes through each node one time"""
        # TODO: Loop through all nodes and count one for each
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        Running time: O(1) because it sets the variable without looping through the nodes"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        n_node = Node(item)

        if self.tail is not None:
            self.tail.next = n_node
            self.tail = n_node
        else:
            self.head = n_node
            self.tail = n_node
        
        return n_node        

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        Running time: O(1) because it sets the variable without looping through the nodes"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        n_node = Node(item)
        
        if self.head is not None:
            n_node.next = self.head
            self.head = n_node
        else:
            self.head = n_node
            self.tail = n_node
        
        return n_node

    def find(self, quality, data):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        Best case runtime: O(1) if the first node is true for quality
        TODO: Worst case running time: O(???) Why and under what conditions?
        Worst case runtime: O(n) if you have to loop through the nodes"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head

        while node is not None:
            if quality(node.data):
                if data:
                    return node.data
                else:
                    return node
            else:
                node = node.next
        
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        Best case runtime: O(1) if the first node is true for deletion
        TODO: Worst case running time: O(???) Why and under what conditions?
        Worst case runtime: O(n) if you have to loop through the nodes"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        node = self.head
        p_node = self.head

        while node is not None:
            if node.data == item:
                if self.length() == 1:
                    self.head = None
                    self.tail = None
                if node == self.head:
                    self.head = node.next
                if node == self.tail:
                    self.tail = p_node

                p_node.next = node.next
                node = None

                return
            elif node != p_node:
                p_node = p_node.next
            node = node.next
        raise ValueError('Item not found: {}'.format(item))

    def replace(self, item, new_item):
        """Replace an existing item with a new one"""
        node = self.find(lambda x: x == item, False)
        node.data = new_item

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
