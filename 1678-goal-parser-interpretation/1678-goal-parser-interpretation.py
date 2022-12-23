class Solution:
    def interpret(self, command: str) -> str:
        index = 0
        size = len(command)
        result = ''
        while size > index:
            if command[index]=='(' and command[index+1] == ')':
                index += 2
                result += 'o'
            elif command[index] != 'G':
                result += 'al'
                index += 4
            else: 
                result += 'G'
                index += 1
        return result
                