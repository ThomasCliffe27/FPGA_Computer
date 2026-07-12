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

cpu.run()

print(cpu.regs)