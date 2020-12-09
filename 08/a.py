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
        while self.ptr not in visited_spaces:
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
        return self.accumulator
    
def a(input):
    instrutions = [ (line.split(' ')[0], int(line.split(' ')[1])) for line in input ]
    aoc = AdventOfComputer(instrutions)
    return aoc.run()
