class Node:
    def __init__(self, length):
        self.length = length
        self.suffixLink = None
        self.next = {}
        self.count = 0

class PalindromeTree:
    def __init__(self, s):
        self.s = s
        self.root1 = Node(-1)  # imaginary root
        self.root2 = Node(0)   # empty string root
        self.root1.suffixLink = self.root1
        self.root2.suffixLink = self.root1
        self.last = self.root2
        self.nodes = [self.root1, self.root2]
        self.build()

    def add_char(self, pos):
        ch = self.s[pos]
        curr = self.last
        while True:
            if pos - curr.length - 1 >= 0 and self.s[pos - curr.length - 1] == ch:
                break
            curr = curr.suffixLink
        if ch in curr.next:
            self.last = curr.next[ch]
            self.last.count += 1
            return
        newNode = Node(curr.length + 2)
        self.nodes.append(newNode)
        curr.next[ch] = newNode
        if newNode.length == 1:
            newNode.suffixLink = self.root2
            newNode.count = 1
            self.last = newNode
            return
        temp = curr.suffixLink
        while True:
            if pos - temp.length - 1 >= 0 and self.s[pos - temp.length - 1] == ch:
                newNode.suffixLink = temp.next[ch]
                break
            temp = temp.suffixLink
        newNode.count = 1
        self.last = newNode

    def build(self):
        for i in range(len(self.s)):
            self.add_char(i)

    def count_distinct_palindromes(self):
        return len(self.nodes) - 2  # exclude the two roots

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    s = "ababa"
    pt = PalindromeTree(s)
    print("Distinct palindromic substrings:", pt.count_distinct_palindromes())  # 5
