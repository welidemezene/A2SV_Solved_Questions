class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Reverse the linked list
        prev, curr = None, head
        while curr:
            next_node = curr.next  # Store the next node
            curr.next = prev  # Reverse pointer
            prev = curr  # Move prev to current
            curr = next_node  # Move current to next node
        head = prev  # Now prev is the new head

        # Step 2: Remove nodes that have a greater value to their left
        max_so_far = head.val  # Keep track of the max value seen so far
        curr = head  # Start from the reversed head
        while curr and curr.next:
            if curr.next.val < max_so_far:
                # Remove the node by skipping it
                curr.next = curr.next.next
            else:
                # Update max_so_far and move forward
                max_so_far = curr.next.val
                curr = curr.next
        
        # Step 3: Reverse the list back to original order
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev  # New head after reversing back