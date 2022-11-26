from dataclasses import dataclass


@dataclass
class Stack:
    elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def top(self):
        return self.elements[-1]

    def bottom(self):
        return self.elements[0]

    def is_empty(self):
        return len(self.elements) == 0


stack = Stack()

print(stack.is_empty())
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))


print(stack.top())
print(stack.bottom())
print(stack.pop())
print(stack.elements)
