class CPU: 
    def __init__(self):
        self.regs = [0] * 16
        self.PC = 0 #Program counter
        self.memory = [0] * 65536
        self.running = True

    def fetch(self):
        instruction = ((self.memory[self.PC] << 24) + 
                       (self.memory[self.PC + 1] << 16) + 
                       (self.memory[self.PC + 2] << 8) + 
                       (self.memory[self.PC + 3]))
        self.PC += 4
        return instruction
    
    def decode_and_execute(self, instruction):
        opcode = (instruction >> 24) & 0xFF

        def parse_I_type_instr(instruction):
            Rx = (instruction >> 20) & 0xF
            imm = (instruction >> 4) & 0xFFFF
            return Rx, imm
        
        def parse_A_type_instr(instruction):
            Rx = (instruction >> 20) & 0xF
            addr = (instruction >> 4) & 0xFFFF
            return Rx, addr
        
        def parse_R_type_instr(instruction):
            Rx = (instruction >> 20) & 0xF
            Ry = (instruction >> 16) & 0xF
            Rz = (instruction >> 12) & 0xF
            return Rx, Ry, Rz

        if opcode == 0x00: #LOADI
            Rx, imm = parse_I_type_instr(instruction)
            self.regs[Rx] = imm

        elif opcode == 0x01: #LOAD
            Rx, addr = parse_A_type_instr(instruction)
            self.regs[Rx] = self.memory[addr]

        elif opcode == 0x10: #STORE
            Rx, addr = parse_A_type_instr(instruction)
            self.memory[addr] = self.regs[Rx]

        elif opcode == 0x20: #ADD
            Rx, Ry, Rz = parse_R_type_instr(instruction)
            self.regs[Rz] = (self.regs[Rx] + self.regs[Ry]) & 0xFFFFFFFF

        elif opcode == 0x21: #SUB
            Rx, Ry, Rz = parse_R_type_instr(instruction)
            self.regs[Rz] = (self.regs[Rx] - self.regs[Ry]) & 0xFFFFFFFF

        elif opcode == 0x30: #AND
            Rx, Ry, Rz = parse_R_type_instr(instruction)
            self.regs[Rz] = self.regs[Rx] & self.regs[Ry]

        elif opcode == 0x31: #OR
            Rx, Ry, Rz = parse_R_type_instr(instruction)
            self.regs[Rz] = self.regs[Rx] | self.regs[Ry]

        elif opcode == 0x32: #XOR
            Rx, Ry, Rz = parse_R_type_instr(instruction)
            self.regs[Rz] = self.regs[Rx] ^ self.regs[Ry]

        elif opcode == 0xFE: #NOP
            pass

        elif opcode == 0xFF: #HALT
            self.running = False

    def run(self):
        while self.running:
            instruction = self.fetch()
            self.decode_and_execute(instruction)