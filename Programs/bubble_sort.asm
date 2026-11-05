// A bubble sort that reads sorts all of the non-zero values stored after mem addr 0x1000
// Each number is just one byte
// Pseudocode:

// sorted = False
// while !sorted:
//   foreach value - 1:
//      sorted = true
//      if value > value + 1
//          sorted = false
//          value + 1 = value
//          value = value + 1

// where value and value + 1 are pointers to the memory addresses

// R0 = 1
// sorted = R1
// value_ptr = R2
// value = R3
// value + 1 = R4

//0x0000
LOADI R0, 0x1
//0x0004
LOADI R1, 0x0
//0x0008
LOADI R2, 0x1000
//0x000C
LOADR R3, R2
//0x0010
ADD R2, R2, R0
//0x0014
LOADR R4, R2


// while !sorted

//0x0018
JUMPR R1, 0x0020
//0x001C
JUMP 0x0090
//0x0020

// for each value
// sorted = true

//0x0024
JUMPR R4, 0x0018
//0x0028
LOADI R1, 0x1




// There is currently no instruction to check whether one value is larger than another I will need to implement it in code

// For any two binary numbers if you cycle through each bit from most to least significant:
// then the number that first has a bit of 1 where the other has a 0 is the larger number

// Pseudocode:
// We want to check if num1 > num2

// num1 = value
// num2 = value + 1
// mask = 0b00000001
// for each bit:
//   num1_bit = num1 & mask
//   num2_bit = num2 & mask
//   if num1_bit - num2_bit == 0:
//     if num1_bit - 1 == 0:
//       is_greater = 1
//     else:
//       is_greater = 0
// mask = mask + mask

//if is_greater = 1 then value > value + 1

// mask = R5
// num1_bit = R6
// num2_bit = R7
// subtraction_results = R8
// is_greater = R9
// loop_tracker = R10


//0x002C
LOADI R5, 0x01
//0x0030
LOADI R10, 0x08
//0x0034
LOADI R9, 0x0
//0x0038
AND R6, R3, R5
//0x003C
AND R7, R4, R5
//0x0040
SUB R8, R6, R7
//0x0044
JUMPR R8, 0x0064
//0x0048
JUMP 0x004C
//0x004C
SUB R8, R6, R5
//0x0050
JUMPR R8, 0x0058
//0x0054
JUMP 0x0060
//0x0058
LOADI R9, 0x1
//0x005C
JUMP 0x0064
//0x0060
LOADI R9, 0x0
//0x0064 
ADD R5, R5, R5
//0x0068
SUB R10, R10, R0
//0x006C
JUMPR R10, 0x0074
//0x0070
JUMP 0x0038


// Now R9 will tell us if value > value + 1
// sorted = false
// swap value and value + 1


//0x0074
JUMPR R9, 0x0024
//0x0078
LOADI R1, 0x0
//0x007C
SUB R2, R2, R0
//0x0080
STORER R4, R2
//0x0084
ADD R2, R2, R0
//0x0088
STORER R3, R2
//0x008C
JUMP 0x0024

//0x0090
HALT