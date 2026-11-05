from cpu import CPU

program = "Programs/bubble_sort.bin"

cpu = CPU()

with open(program, 'rb') as f:
    byte = f.read(1)
    addr = 0
    while byte:
        cpu.memory[addr] = int.from_bytes(byte, byteorder='big')
        addr += 1
        byte = f.read(1)

    cpu.memory[0x1000:0x1033] = [37, 12, 45, 3, 28, 19, 50, 6, 34, 23, 9, 41, 16, 48, 1, 30, 22, 14, 39, 7, 46, 25, 11, 33, 4,
                                 43, 18, 29, 10, 36, 49, 21, 5, 40, 27, 15, 44, 8, 32, 20, 47, 13, 35, 2, 26, 42, 17, 31, 24, 38, 27]
cpu.run()

print(cpu.regs)
print(cpu.memory[0x1000:0x1033])