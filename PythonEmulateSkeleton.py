from ghidra.app.emulator import EmulatorHelper
import struct
from ghidra.program.model.data import Enum
from ghidra.program.model.data import EnumDataType
from ghidra.program.model import listing
from ghidra.program.model.symbol import SourceType
from ghidra.program.disassemble import Disassembler
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.app.plugin.assembler import Assembler
from ghidra.program.model.address import Address, AddressSet
from ghidra.program.model.lang import OperandType
from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface

def main():
  
    FROM = 0x13370000; 
    STATE = 0x13370200; 
    ENCRYPTED_CODE = 0x13370578; 
    LENGTH = 0x00000F96;
    emulator = EmulatorHelper(currentProgram);
    emulator.writeRegister("RIP", 0x7f4a18c8f8e2L);
    emulator.writeRegister("RDI", STATE);
    emulator.writeRegister("RSI", FROM + 4);
    emulator.writeRegister("RDX", FROM + 0x24); 
    emulator.writeRegister("RCX", 0);
    while emulator.getEmulator().getPC() != 0x7f4a18c8f8e7L:
        emulator.step(monitor);
    
    
    state = emulator.readMemory(emulator.getExecutionAddress().getNewAddress(STATE), 0xc0);

    emulator.writeRegister("RIP", 0x7f4a18c8f930L);
    emulator.writeRegister("RDI", STATE); 
    emulator.writeRegister("RSI", ENCRYPTED_CODE);
    emulator.writeRegister("RDX", LENGTH);
    while emulator.getEmulator().getPC() != 0x7f4a18c8f935L: 
        emulator.step(monitor);

    code = emulator.readMemory(emulator.getExecutionAddress().getNewAddress(ENCRYPTED_CODE), LENGTH);
    print(code)
    print(code)
    
    with open (r"C:\Users\IEUser\Documents\output.bin","ab+") as output:
        output.write(code)
        
if __name__ == "__main__":
        main()

   
