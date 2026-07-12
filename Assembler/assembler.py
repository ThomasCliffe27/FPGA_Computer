from instr_to_bin import instr_to_bin

def assemble(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    binary_instructions = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            binary_instruction = instr_to_bin(line)
            binary_instructions.append(binary_instruction)

    with open(output_file, 'wb') as f:
        for instruction in binary_instructions:
            f.write(instruction.to_bytes(4, byteorder='big'))


if __name__ == "__main__":
    input_file = 'Programs/program.asm'
    output_file = 'Programs/program.bin'
    assemble(input_file, output_file)
    print(f"Assembly complete. Binary output written to {output_file}.")