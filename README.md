# FPGA Computer

## Goals
My aim with this project is to help me understand how computers work at a low level by exploring computer architecture and designing a custom CPU which i will initially create an emulator for in Python before implementing it on an FPGA.

## Current status
- [x] Custom ISA designed
- [ ] Emulator made in Python
- [ ] An assembler for my custom ISA
- [ ] Design implemented on an FPGA
- [ ] Adding I/O to my FPGA computer (UART, VGA, PS/2)
- [ ] A compiler for my custom ISA?
- [ ] An basic OS for my computer?

## Documentation
I have chosen a 32 bit architecture for my CPU because I think it is a good balance between not being too limited to make an OS/compiler, and using more FPGA resources with minimal benefit as I cannot forsee needing more than the ~4GB of memory space 32 bits gives me or needing to frequently perform large calculations.

For a first simple version there will be:
- 16 32-Bit registers
- 65526 Bytes of RAM
- Von Neumann architecture

### ISA
For the first version of my ISA i have decided to keep it very simple with just enough instructions to run very simple linear programs. The ISA is outined below. 

The instructions may contain some abbreviations which i have shown below.
| Abbreviation | Example | Description| 
|--------------|---------|------------|
|Rx            |R7       |Refers to register number x e.g. register 7|
|addr          |0x1234   |Refers to location in memory|
|#imm          |#0x12 / #0d18 / #0b10010|Refers to a hex/dec/bin number|


|      Instruction      | Description| 
|-----------------------|------------|
|LOADI Rx, #imm         |Loads an immediate into a register|
|LOAD Rx, addr          |Loads the byte stored in the memory address into the lowest 8 bits of the register|
|STORE Rx, addr         |Stores the lowest 8 bits of the register into the memory address|
|ADD Rx, Ry, Rz         |Adds Rx and Ry together and stores it in Rz|
|SUB Rx, Ry, Rz         |Subtracts Ry from Rx and stores the result in Rz|
|AND Rx, Ry, Rz         |Stores the bitwise result of Rx & Ry in Rz|
|OR Rx, Ry, Rz          |Stores the bitwise result of Rx | Ry in Rz|
|XOR Rx, Ry, Rz         |Stores the bitwise result of Rx ^ Ry in Rz|
|NOP                    |Nothing happens|
|HALT                   |Stops operation of the CPU|

### Instruction encoding
For simplicity the first version of my CPU will have a fixed 32 bit instruction length but later I will adapt it to use a variable instruction length for a smaller program size.

To start there will be 4 different types of instruction:
- I-type(immediate) e.g. LOADI Rx, #imm
- A-type(address) e.g. LOAD Rx, addr
- R-type(register) e.g. ADD Rx, Ry, Rz
- B-type(blank) e.g. NOP

The encoding for each type of instruction is as follows:
- I-Type
| Bits | Purpose |
|------|---------|
|0-7   |Opcode |
|8-11  |Rx |
|12-27 |16-bit immediate |
|28-31 |Unused |


- A-Type
| Bits | Purpose |
|------|---------|
|0-7   |Opcode |
|8-11  |Rx |
|12-27 |16-bit address |
|28-31 |Unused |


- R-Type
| Bits | Purpose |
|------|---------|
|0-7   |Opcode |
|8-11  |Rx |
|12-15 |Ry |
|16-19 |Rz |
|20-31 |Unused |


- B-Type
| Bits | Purpose |
|------|---------|
|0-7   |Opcode |
|8-31  |Unused |