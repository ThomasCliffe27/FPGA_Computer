from cpu import CPU

program = "Programs/program.bin"

cpu = CPU()

with open(program, 'rb') as f:
    byte = f.read(1)
    addr = 0
    while byte:
        cpu.memory[addr] = int.from_bytes(byte, byteorder='big')
        addr += 1
        byte = f.read(1)

    cpu.memory[1000] = 1
    cpu.memory[1001] = 5
    cpu.memory[1002] = 2
    cpu.memory[1003] = 3
cpu.run()

print(cpu.regs)
print(cpu.memory[1000], cpu.memory[1001], cpu.memory[1002], cpu.memory[1003])