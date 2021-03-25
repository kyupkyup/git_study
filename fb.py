

class FizzBuzz:
    def __init__(self, n):
        self.number = n

    def return_fizz():
        pass

    def return_buzz():
        pass

    def return_rest():
        pass

n = int(input())
fb = FizzBuzz(n)

answer = ""
if fb.return_fizz():
    answer += "fizz"

if fb.return_buzz():
    answer += "buzz"

if not fb.return_fizz() and not fb.return_buzz():
    answer = str(n)

print(answer)
i






