from cpu import CPU

cpu = CPU()

# Program:
# LOADI R1, 6
# LOADI R2, 21
# ADD R1, R2, R3
# HALT

cpu.memory[0] = 0x00
cpu.memory[1] = 0x10
cpu.memory[2] = 0x00
cpu.memory[3] = 0x60

cpu.memory[4] = 0x00
cpu.memory[5] = 0x20
cpu.memory[6] = 0x01
cpu.memory[7] = 0x50

cpu.memory[8] = 0x20
cpu.memory[9] = 0x12
cpu.memory[10] = 0x30
cpu.memory[11] = 0x00

cpu.memory[12] = 0xFF
cpu.memory[13] = 0x00
cpu.memory[14] = 0x00
cpu.memory[15] = 0x00

cpu.run()

print(cpu.regs)