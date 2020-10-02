# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
class Regex():
    def __init__(self, uid):
        self.uid = uid
    
    def check_validity(self):
        s = set(uid)
        if len(s) == 10 and len(re.findall('[A-Z]', uid)) >= 2 and len(re.findall('[0-9]', uid)) >= 3:
           print('Valid')
        else:
            print('Invalid')


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        uid = input()
        my_object = Regex(uid)
        my_object.check_validity()

