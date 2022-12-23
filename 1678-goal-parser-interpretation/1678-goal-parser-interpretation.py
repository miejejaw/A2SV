class Solution:
    def interpret(self, command: str) -> str:
        index = 0
        size = len(command)
        result = ''
        while size > index:
            if command[index:index+2]=='()':
                index += 2
                result += 'o'
            elif command[index] == 'G':
                result += 'G'
                index += 1
            else: 
                result += 'al'
                index += 4
        return result
                