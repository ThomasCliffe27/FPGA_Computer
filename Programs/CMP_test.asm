LOADI R0, 0x5
LOADI R1, 0x6
CMP R0, R1
JUMPC R1_Bigger
LOADI R3, 0x0
JUMP Program_End

label R1_Bigger
    LOADI R3, 0x1
    JUMP Program_End

label Program_End
    HALT