"""
-------------------------------------------------------
List Linked
-------------------------------------------------------
Author:  Iman Chaudhry
__updated__ = "2023-03-03"
-------------------------------------------------------
"""
from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = _List_Node(value, self._front) # for count 0, self._front is None, otherwise next is self._front bc prepend
        
        if self._count == 0:
            self._rear = self._front # when count is 1, front = rear
            
        self._count += 1
        
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _List_Node(value, None)
        
        if self._count == 0:
            self._front = node
            self._rear = self._front
        else:
            self._rear._next = node
            self._rear = self._rear._next
            
        self._count += 1 
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._count == 0 or i < -len(self) or i == 0:
            self.prepend(value)
            
        elif self._count == i or i > (len(self)-1):
            self.append(value)
            
        else:
            curr = self._front
            index = 0
            while index < (i-1):
                curr = curr._next
                index += 1
            curr._next = _List_Node(value, curr._next)
            self._count += 1
            
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        index = 0
        current = self._front
        previous = None
        
        while current is not None and current._value != key:
            previous = current
            current = current._next
            index  += 1
            
        if current is None:
            index = -1
            
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search(key)
        if index == -1:
            value = None
        else:
            value = current._value
            if index == 0 and self._count > 1:
                self._front = self._front._next            
            elif self._count == 1:
                self._front = None
                self._rear = self._front
            elif index == (self._count - 1):
                previous._next = None
                self._rear = previous
            else:
                previous._next = current._next
            self._count -= 1
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        value = self._front._value
        self._count -= 1
        
        if self._count == 1:
            self.rear = self._front
        if self._count == 0:
            self._rear = None
            
        self._front = self._front._next
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
#        previous, current, index = self._linear_search(key)
#        while index != -1:
#            if index == 0 and self._count > 1:
#                self._front = self._front._next            
#            elif self._count == 1:
#                self._rear = None
#                self._front = self._rear
#            elif index == (self._count - 1):
#                previous._next = None
#                self._rear = previous
#            else:
#                previous._next = current._next
#            self._count -= 1
#            previous, current, index = self._linear_search(key)

        _, _, index = self._linear_search(key)
        
        while index > -1:
            _, _, index = self._linear_search(key)
            self.remove(key)

        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, index = self._linear_search(key)
        value = None
        if index != -1:
            value = current._value
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        value = deepcopy(self._front._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        _, _, index = self._linear_search(key)
        return index

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        
        if i < 0:
            i += len(self)
        
        curr = self._front
        for _ in range(i):
            curr = curr._next
            
        value = curr._value
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        curr = self._front
        
        if i >= 0:
            count = 0
        else:
            count = self._count * -1
            
        while count < i:
            curr = curr._next
            count += 1
        curr._value = deepcopy(value)
        return 

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        *_, index = self._linear_search(key)
        
        return index > -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: max_value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        i = 1
        curr = self._front
        max_data = self._front._value
        
        while i < self._count:
            if curr._next._value > max_data:
                max_data = curr._next._value
                
            curr = curr._next
            i += 1
        
        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        i = 1
        curr = self._front
        min_data = self._front._value
        
        while i < self._count:
            if curr._next._value < min_data:
                min_data = curr._next._value
                
            curr = curr._next
            i += 1
        
        return min_data

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        curr = self._front
        number = 0
        i = 0
        
        while i < self._count:
            if curr._value == key:
                number += 1
            curr = curr._next
            i += 1    
        
        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._rear = self._front
        prev = None
        curr = self._front
        
        while curr is not None:
            temp = curr._next
            curr._next = prev 
            prev = curr
            curr = temp
            
        self._front = prev
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        if self._front is not None:
            self._reverse_r_aux(None, self._front)
            self._front, self._rear = self._rear, self._front
        return

    def _reverse_r_aux(self, prev, curr):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        if curr is None:
            self._front = prev
        else:
            temp = curr._next
            curr._next = prev 
            prev = curr
            curr = temp
            self.reverse_r_aux(prev, curr)
        
        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        prev = None
        curr = self._front
 
        while curr is not None and curr._next is not None:
            prev = curr
            while prev._next is not None:
                if curr._value == prev._next._value:
                    prev._next = prev._next._next
                    self._count -= 1
                else:
                    prev = prev._next
 
            curr = curr._next
            
        if self._count == 1:
            self._front = self._rear
            
        return
    
    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        left = None
        right = None
        
        if pln != prn:
            if pln is None:
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next
                
            if prn is None:
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left
        
            temp = left._next
            left._next = right._next
            right._next = temp
            
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
            
        return

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals = True
        if self._count == target._count:
            curr = self._front
            tar = target._front
            while curr is not None and tar is not None and equals is not False:
                if curr._value == tar._value:
                    curr = curr._next
                    tar = tar._next
                else:
                    equals = False
        else:
            equals = False
            
        return equals

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical

    def is_identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            other - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if other._count != self._count:
            identical = False

        else:
            identical = self.is_identical_r_aux(self._front, other._front)
            
        return identical

    def is_identical_r_aux(self, source_node, other_node):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            other - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if source_node is None:
            identical = True #end of list reached
        elif source_node._value != other_node._value:
            identical = False 
        else:
            identical = self.is_identical_r_aux(source_node._next, other_node._next)
        
        return identical

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        
        mid = self._count // 2 + self._count % 2
        count = 0
        while count is not mid:
            target1._move_front_to_rear(self)
            count += 1
            
        while self._front is not None:
            target2._move_front_to_rear(self)
        
        self._front = None
        self._rear = None
        self._count = 0
        
        return target1, target2
    

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source self is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
            
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        even = List()
        odd = List()
        self._split_alt_r_aux(even, odd, True)
        return even, odd

    def _split_alt_r_aux(self, target1, target2, left):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
        -------------------------------------------------------
        """
        if self._count > 0:
            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
            self._split_alt_r_aux(target1, target2, left)
        return

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        if self._front is not None:
            c = self._front
            i = 0
            p = None
            if c._value == key:
                previous = None
                current = c
                index = i
            else:
                previous, current, index = self._linear_search_r_aux(i, c, p, key)
        else:
            previous = None
            current = None
            index = -1
            
        return previous, current, index

    def _linear_search_r_aux(self, i, c, p, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        if c is None or c._value == key:
            current = c
            previous = p
            if current is not None:
                index = i
            else:
                index = -1
        else:
            p = c
            c = c._next
            i += 1
            previous, current, index = self._linear_search_r_aux(i, c, p, key)
        return previous, current, index
    
    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self.append(value)

            source1_node = source1_node._next
        return

    def intersection_clean(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        curr1 = source1._front
        
        while curr1 is not None:
            value = curr1._value
            if value in source2:
                self.append(value)
                
            curr1 = curr1._next
                
        self.clean()
        return
    
    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        if source1._front is not None and source2._front is not None:
            index = 0
            self.intersection_r_aux(index, source1._front, source1, source2)
        
        #curr = source1._front
        #self.intersection_r_aux(curr, source2)
        return
    
    def intersection_r_aux(self, index, current, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if index < source1._count:
            *_, i = source2._linear_search(current._value)
            if i > -1:
                *_, i = self._linear_search(current._value)
                if i == -1:
                    self.append(current._value)
            index += 1
            self.intersection_r_aux(index, current._next, source1, source2)

        #if curr is None:
        #    self.clean()
        #else:
        #    value = curr._value
        #    if value in source2:
        #        self.append(value)
        #    self.intersection_r_aux(curr._next, source2)
        return
    

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        node._next = self._front
        self._front = node

        if self._rear is None:
            # Target list is empty
            self._rear = node
        self._count += 1
        
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                self.append(value)
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                self.append(value)
            source2_node = source2_node._next
        return

    def union_clean(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        curr1 = source1._front
        curr2 = source2._front
        
        while curr1 is not None:
            value1 = curr1._value
            self.append(value1)
            curr1 = curr1._next

        while curr2 is not None:
            value2 = curr2._value
            self.append(value2)
            curr2 = curr2._next
            
        self.clean()
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        if source1._front is not None:
            index = 0
            select = 0
            self.union_r_aux(select, index, source1._front, source1, source2)
        else:
            if source2._front is not None:
                index = 0
                select = 1
                self.union_r_aux(select, index, source2._front, source1, source2)
        return

    def union_r_aux(self, select, index, current, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if select == 0:
            *_, i = self._linear_search(current._value)
            if i == -1:
                self.append(current._value)
            index += 1
            if index < source1._count:
                self.union_r_aux(select, index, current._next, source1, source2)
            else:
                select = 1
                index = 0
                self.union_r_aux(select, index, source2._front, source1, source2)
        else:
            if current is not None:
                *_, i = self._linear_search(current._value)
                if i == -1:
                    self.append(current._value)
                index += 1
                if index < source2._count:
                    self.union_r_aux(select, index, current._next, source1, source2)
        return

    def union_r_aux_clean(self, curr1, curr2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if curr1 is None and curr2 is None:
            self.clean()
        else:
            if curr1 is not None:
                value1 = curr1._value
                self.append(value1)
                self.union_r_aux(curr1._next, None)
        
            if curr2 is not None:
                value2 = curr2._value
                self.append(value2)
                self.union_r_aux(None, curr2._next)               
            
        return

    def union_r_clean(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self.union_r_aux(source1._front, source2._front)
        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        self.clean_r_aux(self._front, None, self._front._next, self._front._next)
        if self._count == 1:
            self._front = self._rear
        return

    def clean_r_aux(self, curr, prev, pnext, cnext):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
            
        if curr is not None and cnext is not None:
            prev = curr
            if pnext is None:
                self.clean_r_aux(curr._next, prev, None, cnext._next)
            else:
                if curr._value == pnext._value:
                    self.clean_r_aux(curr, prev, pnext._next, cnext)
                else:
                    self.clean_r_aux(curr, prev._next, pnext, cnext)
                    
        return  

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        if self._front is not None:
            # Initialize both temporary pointers to beginning of the list.
            tortoise = self._front
            hare = self._front

            while hare is not None and hare._next is not None:
                # Move hare down two nodes.
                hare = hare._next._next

                if hare is not None:
                    # Update tortoise only if hare is not None.
                    tortoise = tortoise._next

            # Set up target lists
            target1._front = self._front
            target1._rear = tortoise
            target2._front = tortoise._next
            tortoise._next = None
            target2._count = self._count // 2
            target1._count = self._count - target2._count

            if target2._count > 0:
                target2._rear = self._rear
            # Clean up source
            self._count = 0
            self._front = None
            self._rear = None

        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish, self
        is empty.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        
        
        while self._front is not None:
            if self._front._value < key:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            
        return target1, target2

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        new_list = List()
        
        curr = self._front
        
        while curr is not None:
            new_list.append(curr._value)
            curr = curr._next
            
        return new_list

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        new_list = List()
        self.copy_r_aux(self._front, new_list)
        return new_list

    def copy_r_aux(self, curr, new_list):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive version)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        if curr is not None:
            new_list.append(curr._value)
            self.copy_r_aux(curr._next, new_list)
        return new_list

    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        # Split the list into two halves
        slow = self._front
        fast = self._front._next
        while fast is not None and fast._next is not None:
            slow = slow._next
            fast = fast._next._next
        mid = slow._next
        slow._next = None
        
        # Reverse the second half of the list
        prev = None
        curr = mid
        while curr is not None:
            next = curr._next
            curr._next = prev
            prev = curr
            curr = next
        second = prev
        
        # Merge the two halves of the list
        first = self._front
        while second is not None:
            next_first = first._next
            next_second = second._next
            first._next = second
            second._next = next_first
            first = next_first
            second = next_second
 
        
        return


    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"
        
        node = source._front
        if self._rear is None:
            self._front = node
            self._rear = node
            
        else:
            self._rear._next = node
            self._rear = node
            
        if source._front == source._rear:
            source._front = None
            source._rear = None
            
        else:
            source._front = source._front._next
            
        source._count -= 1
        self._count += 1
        self._rear._next = None
        
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1._count > 0 and source2._count > 0:
            self._move_front_to_rear(source1)
            self._move_front_to_rear(source2)
            
        while source1._count > 0:
            self._move_front_to_rear(source1)
            
        while source2._count > 0:
            self._move_front_to_rear(source2)
            
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self.combine_r_aux(source1, source2)
        
        return

    def combine_r_aux(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if source1._count == 0 and source2._count > 0:
            self._move_front_to_rear(source2)
                
        if source2._count == 0 and source1._count > 0:
            self._move_front_to_rear(source1)
                
        else:
            if source1._count > 0:
                self._move_front_to_rear(source1)
            if source2._count > 0:
                self._move_front_to_rear(source2)
            
            self.combine_r_aux(source1, source2)              
            
        return

    def _append(self, value):
        """
        ---------------------------------------------------------
        Helper method to add a copy of value to the end of the List.
        Use: self._append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def _append_list(self, source):
        """
        -------------------------------------------------------
        Helper method to append the entire source list to the rear of the target list.
        The source list becomes empty.
        Use: target._append_list(source)
        -------------------------------------------------------
        Parameters:
            source - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        # Update the target list
        if self._rear is None:
            # Current list is empty.
            self._front = source._front
        else:
            self._rear._next = source._front

        self._rear = source._rear
        self._count += source._count
        # Empty the source list.
        source._front = None
        source._rear = None
        source._count = 0
        return
    
    def clear(self):
        """
        -------------------------------------------------------
        Clears the linked list
        Use: source.clear()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next