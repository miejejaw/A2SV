class Solution:
    def interpret(self, command: str) -> str:
        index = 0
        size = len(command)
        while size > index:
            if command[index]=='(' and command[index+1] == ')':
                command = command[:index]+"o"+command[index+2:]
                size -= 1
            elif command[index] != 'G':
                command = command[:index]+"al"+command[index+4:]
                size -= 2
                index += 1
            index += 1
        return command
                