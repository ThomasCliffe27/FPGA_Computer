# FPGA Computer

## Goals
My aim with this project is to help me understand how computers work at a low level by exploring computer architecture and designing a custom CPU which i will initially create an emulator for in Python before implementing it on an FPGA.

## Current status
- [x] Custom ISA designed
- [x] Emulator made in Python
- [x] An assembler for my custom ISA
- [ ] Design implemented on an FPGA
- [ ] Adding I/O to my FPGA computer (UART, VGA, PS/2)
- [ ] A compiler for my custom ISA?
- [ ] An basic OS for my computer?

## Documentation
I have chosen a 32 bit architecture for my CPU because I think it is a good balance between not being too limited to make an OS/compiler, and using more FPGA resources with minimal benefit as I cannot forsee needing more than the ~4GB of memory space 32 bits gives me or needing to frequently perform large calculations.

For a first simple version there will be:
- 16 32-Bit registers
- 65536 Bytes of RAM (2 ^ 16)
- Von Neumann architecture

### ISA
For the first version of my ISA i have decided to keep it very simple with just enough instructions to run very simple programs. The ISA is outined below. 

The instructions may contain some abbreviations which i have shown below.
| Abbreviation | Example | Description| 
|--------------|---------|------------|
|Rx            |R7       |Refers to register number x e.g. register 7|
|addr          |0x1234   |Refers to location in memory|
|#imm          |#0x12 / #0d18 / #0b10010|Refers to a hex/dec/bin number|


| Instruction    | Opcode| Type  |Description|
|----------------|-------|-------|-----------|
|LOADI Rx, imm   |0x00   |I-Type |Loads an immediate value into a register|
|LOAD Rx, addr   |0x01   |A-Type |Loads the byte stored at a memory address into the lowest 8 bits of the register|
|STORE Rx, addr  |0x10   |A-Type |Stores the lowest 8 bits of the register into a memory address|
|ADD Rx, Ry, Rz  |0x20   |R-Type |Adds Ry and Rz together and stores the result in Rx|
|SUB Rx, Ry, Rz  |0x21   |R-Type |Subtracts Rz from Ry and stores the result in Rx|
|AND Rx, Ry, Rz  |0x30   |R-Type |Stores the bitwise result of Ry & Rz in Rx|
|OR Rx, Ry, Rz   |0x31   |R-Type |Stores the bitwise result of Ry | Rz in Rx|
|XOR Rx, Ry, Rz  |0x32   |R-Type |Stores the bitwise result of Ry ^ Rz in Rx|
|NOT Rx, Ry      |0x33   |R-Type |Stores the bitwise result of ~Ry in Rx|
|JUMP addr       |0x40   |A-Type |Sets the PC to the address stated|
|JUMPR Rx, addr  |0x41   |A-Type |Sets the PC to the address stated if Rx == 0|
|NOP             |0xFE   |B-Type |Performs no operation|
|HALT            |0xFF   |B-Type |Stops execution of the CPU|

### Instruction encoding
For simplicity the first version of my CPU will have a fixed 32 bit instruction length but later I will adapt it to use a variable instruction length for a smaller program size.

To start there will be 4 different types of instruction:
- I-type(immediate) e.g. LOADI Rx, #imm
- A-type(address) e.g. LOAD Rx, addr or JUMP addr(where Rx will be blank)
- R-type(register) e.g. ADD Rx, Ry, Rz or NOT Rx, Ry(where Rz will be blank)
- B-type(blank) e.g. NOP

The encoding for each type of instruction is as follows:
#### I-Type
| Bits | Purpose |
|------|---------|
|0-7   |Opcode |
|8-11  |Rx |
|12-27 |16-bit immediate |
|28-31 |Unused |


#### A-Type
| Bits | Purpose |
|------|---------|
|0-7   |Opcode |
|8-11  |Rx or unused depending on instruction|
|12-27 |16-bit address |
|28-31 |Unused |


#### R-Type
| Bits | Purpose |
|------|---------|
|0-7   |Opcode |
|8-11  |Rx |
|12-15 |Ry |
|16-19 |Rz or unused depending on instruction|
|20-31 |Unused |


#### B-Type
| Bits | Purpose |
|------|---------|
|0-7   |Opcode |
|8-31  |Unused |