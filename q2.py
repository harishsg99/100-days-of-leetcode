class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        i = 0
        root = res_list = ListNode(0)
        while l1 is not None:
            num1 += l1.val * pow(10, i)
            i += 1
            l1 = l1.next
        i = 0
        while l2 is not None:
            num2 += l2.val* pow(10, i)
            i += 1
            l2 = l2.next
        res = num1 + num2
        if res == 0:
            return root
        while res != 0:
            # res_list.append(res % 10)
            res_list.next = ListNode(res % 10)
            res_list = res_list.next
            res //= 10
        return root.next
    
