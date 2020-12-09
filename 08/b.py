class AdventOfComputer:
    def __init__(self, instructions):
        self.accumulator = 0
        self.instructions = instructions
        self.ptr = 0
    def acc(self, i):
        self.accumulator += i
    def jmp(self, i):
        self.ptr += i
    def nop(self, i):
        # do nothing
        pass
    def run(self):
        visited_spaces = set()
        while self.ptr not in visited_spaces and self.ptr < len(self.instructions):
            visited_spaces.add(self.ptr)
            instr = self.instructions[self.ptr]
            if instr[0] == 'acc':
                self.acc(instr[1])
                self.ptr += 1
            elif instr[0] == 'jmp':
                self.jmp(instr[1])
            elif instr[0] == 'nop':
                self.nop(instr[1])
                self.ptr += 1
            else:
                print("i didn't know that instruction")
            if self.ptr in visited_spaces:
                return None
        return self.accumulator

def b(input):

    instructions = [ (line.split(' ')[0], int(line.split(' ')[1])) for line in input ]
    for i in range(len(instructions)):
        if instructions[i][0] == 'nop':
            instructions[i] = ('jmp', instructions[i][1])
        elif instructions[i][0] == 'jmp':
            instructions[i] = ('nop', instructions[i][1])
        aoc = AdventOfComputer(instructions)
        result = aoc.run()
        if result:
            return result
        if instructions[i][0] == 'nop':
            instructions[i] = ('jmp', instructions[i][1])
        elif instructions[i][0] == 'jmp':
            instructions[i] = ('nop', instructions[i][1])
