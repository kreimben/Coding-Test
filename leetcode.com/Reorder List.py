"""
https://leetcode.com/problems/reorder-list/
Reorder List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def get_inner_values(node: ListNode) -> [int]:
    curr = node
    results = []
    while curr:
        results.append(curr.val)
        curr = curr.next

    return results


def deploy_values(node: ListNode, values: [int]):
    curr = node
    index = 0
    while curr:
        curr.val = values[index]
        index += 1
        curr = curr.next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        values: [int] = get_inner_values(head)
        mid_index = len(values) // 2
        index = 1  # The number being inserted should be inserted right next first element of originals.

        while index <= mid_index:
            last = values.pop()
            values.insert(index, last)
            index += 2
            mid_index += 1

        deploy_values(head, values)


s = Solution()
input_node = ListNode(1,
                      ListNode(2,
                               ListNode(3,
                                        ListNode(4,
                                                 ListNode(5)
                                                 )
                                        )
                               )
                      )
s.reorderList(
    input_node
)
expected = ListNode(1,
                    ListNode(5,
                             ListNode(2,
                                      ListNode(4,
                                               ListNode(3)
                                               )
                                      )
                             )
                    )
assert input_node == expected
