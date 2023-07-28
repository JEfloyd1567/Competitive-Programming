from sys import stdin

def solve(string):
    stack = []
    ans = True
    i = 0
    while(i < len(string) and ans):
        
        if(string[i] == '(' or string[i] == '['):
            stack.append(string[i])

        elif(string[i] == ')' or string[i] == ']'):

            if(string[i] == ')' and len(stack) > 0 and stack[-1] == '('):
                stack.pop()

            elif(string[i] == ']'and len(stack) > 0 and stack[-1] == '['):
                stack.pop()
            else:
                ans = False
        i += 1

    if(len(stack) > 0):
        ans = False

    return ans


def main():
    cases = int(input())
    for i in range(cases):
        string = stdin.readline()
        if(solve(string)):
            print("Yes")
        else:
            print("No")
main()
