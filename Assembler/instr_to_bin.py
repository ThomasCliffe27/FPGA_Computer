def instr_to_bin(instruction):
    parts = instruction.split()
    parsed_parts = []

    for part in parts:
        part = part.strip(', ')

        if part.startswith("R"):
            part = part[1:]
        elif part.startswith("#"):
            part = part[1:]

        if part.startswith('0x'):
            part = int(part[2:], 16)
        elif part.startswith('0b'):
            part = int(part[2:], 2)
        elif part.startswith('0d'):
            part = int(part[2:], 10)
        elif part.isdigit():
            part = int(part)
        
        parsed_parts.append(part)

    opcode = parts[0].upper()

    def parse_I_type_instr(parts, opcode):
        Rx = int(parts[1])
        imm = int(parts[2])
        instruction = (opcode << 24) + (Rx << 20) + ((imm & 0xFFFF) << 4)
        return instruction

    def parse_A_type_instr(parts, opcode):
        Rx = int(parts[1])
        addr = int(parts[2])
        instruction = (opcode << 24) + (Rx << 20) + ((addr & 0xFFFF) << 4)
        return instruction

    def parse_R_type_instr(parts, opcode):
        Rx = int(parts[1])
        Ry = int(parts[2])
        Rz = int(parts[3])
        instruction = (opcode << 24) + (Rx << 20) + (Ry << 16) + (Rz << 12)
        return instruction

    if opcode == "LOADI":
        opcode = 0x00
        return parse_I_type_instr(parsed_parts, opcode)

    elif opcode == "LOAD":
        opcode = 0x01
        return parse_A_type_instr(parsed_parts, opcode)

    elif opcode == "STORE":
        opcode = 0x10
        return parse_A_type_instr(parsed_parts, opcode)

    elif opcode == "ADD":
        opcode = 0x20
        return parse_R_type_instr(parsed_parts, opcode)

    elif opcode == "SUB":
        opcode = 0x21
        return parse_R_type_instr(parsed_parts, opcode)

    elif opcode == "AND":
        opcode = 0x30
        return parse_R_type_instr(parsed_parts, opcode)

    elif opcode == "OR":
        opcode = 0x31
        return parse_R_type_instr(parsed_parts, opcode)

    elif opcode == "XOR":
        opcode = 0x32
        return parse_R_type_instr(parsed_parts, opcode)

    elif opcode == "NOP":
        opcode = 0xFE
        return opcode << 24

    elif opcode == "HALT":
        opcode = 0xFF
        return opcode << 24