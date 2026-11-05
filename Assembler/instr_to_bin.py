def instr_to_bin(instruction):
    parts = instruction.split()
    parsed_parts = []

    for part in parts:
        part = part.strip(', ')

        if part.startswith("R"):
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

    def parse_A_type_instr(parts, opcode, addr_or_reg): #addr_or_reg = 0 for addr, 1 for reg
        if len(parts) > 2:
            if addr_or_reg:
                Rx = int(parts[1])
                addr = 0
                Ry = int(parts[2])
            else:
                Rx = int(parts[1])
                addr = int(parts[2])
                Ry = 0
        else:
            Rx = 0  # Default value for Rx if not given e.g. JUMP addr
            addr = int(parts[1])
            Ry = 0
        instruction = (opcode << 24) + (Rx << 20) + ((addr & 0xFFFF) << 4) + Ry
        return instruction

    def parse_R_type_instr(parts, opcode):
        Rx = int(parts[1])
        Ry = int(parts[2])
        if len(parts) > 3:
            Rz = int(parts[3])
        else:
            Rz = 0  # Default value for Rz if not given e.g. NOT Rx, Ry
        instruction = (opcode << 24) + (Rx << 20) + (Ry << 16) + (Rz << 12)
        return instruction

    if opcode == "LOADI":
        opcode = 0x00
        return parse_I_type_instr(parsed_parts, opcode)

    elif opcode == "LOADA":
        opcode = 0x01
        return parse_A_type_instr(parsed_parts, opcode, 0) # addr_or_reg = 0 for address

    elif opcode == "LOADR":
        opcode = 0x02
        return parse_A_type_instr(parsed_parts, opcode, 1) # addr_or_reg = 1 for register
    
    elif opcode == "STOREA":
        opcode = 0x10
        return parse_A_type_instr(parsed_parts, opcode, 0)

    elif opcode == "STORER":
        opcode = 0x11
        return parse_A_type_instr(parsed_parts, opcode, 1)

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

    elif opcode == "NOT":
        opcode = 0x33
        return parse_R_type_instr(parsed_parts, opcode)
    
    elif opcode == "JUMP":
        opcode = 0x40
        return parse_A_type_instr(parsed_parts, opcode, 0) # addr_or_reg does not matter here

    elif opcode == "JUMPR":
        opcode = 0x41
        return parse_A_type_instr(parsed_parts, opcode, 0) # addr_or_reg = 0 for address

    elif opcode == "NOP":
        opcode = 0xFE
        return opcode << 24

    elif opcode == "HALT":
        opcode = 0xFF
        return opcode << 24
    
    else:
        raise ValueError(f"Unknown instruction: {opcode}")