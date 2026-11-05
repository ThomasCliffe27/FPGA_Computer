from instr_to_bin import instr_to_bin

def assemble(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        labels = dict()
        mem_pos = 0
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line and not cleaned_line.startswith("//"):
                mem_pos += 4
                if line.startswith("label"):
                    mem_pos -= 4
                    labels[line.strip().removeprefix("label ").removesuffix(":")] = mem_pos

        print("Labels:")
        for label in labels:
            print(label, labels[label])


    with open(input_file, 'r') as f:
        lines = f.readlines()

    binary_instructions = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("label") and not line.startswith('//'):
            print(f"Processing line: {line}")
            binary_instruction = instr_to_bin(line, labels)
            binary_instructions.append(binary_instruction)

    with open(output_file, 'wb') as f:
        for instruction in binary_instructions:
            f.write(instruction.to_bytes(4, byteorder='big'))


if __name__ == "__main__":
    input_file = 'Programs/program.asm'
    output_file = 'Programs/program.bin'
    assemble(input_file, output_file)
    print(f"Assembly complete. Binary output written to {output_file}.")
