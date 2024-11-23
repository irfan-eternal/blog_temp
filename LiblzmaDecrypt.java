import ghidra.app.emulator.EmulatorHelper;
import ghidra.app.script.GhidraScript;
import ghidra.app.util.opinion.ElfLoader;
import ghidra.pcode.emulate.EmulateExecutionState;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.symbol.*;
import ghidra.util.Msg;
import ghidra.util.exception.NotFoundException;
import java.io.*;

public class LiblzmaDecrypt extends GhidraScript {
    @Override
    public void run() throws Exception {
        long FROM = 0x13370000; // <-- Address of FROM parameter data
        long STATE = 0x13370200; // <-- Address to store the resulting chacha state in.

        long ENCRYPTED_CODE = 0x0; // <-- Address to put the encrypted/decrypted code buffer at.
        long LENGTH = 0x00000F96;

        println("Running");

        var emulator = new EmulatorHelper(currentProgram);

        // Call chacha_init
        emulator.writeRegister("RIP", 0x7f4a18c8f8e2L);
        emulator.writeRegister("RDI", STATE);
        emulator.writeRegister("RSI", FROM + 4);
        emulator.writeRegister("RDX", FROM + 0x24); 
        emulator.writeRegister("RCX", 0);
        while (emulator.getEmulator().getPC() != 0x7f4a18c8f8e7L) // Execute till return
            emulator.step(monitor);
        
        // Read out the init buffer.
        byte[] state = emulator.readMemory(emulator.getExecutionAddress().getNewAddress(STATE), 0xc0);

        // Call chacha_encrypt_decrypt
        emulator.writeRegister("RIP", 0x7f4a18c8f930L);
        emulator.writeRegister("RDI", STATE); 
        emulator.writeRegister("RSI", ENCRYPTED_CODE);
        emulator.writeRegister("RDX", LENGTH);
        while (emulator.getEmulator().getPC() != 0x7f4a18c8f935L) // Execute till return
            emulator.step(monitor);

        // Read out the decrypted code memory.
        byte[] code = emulator.readMemory(emulator.getExecutionAddress().getNewAddress(ENCRYPTED_CODE), (int) LENGTH);
        FileOutputStream out = new FileOutputStream("/tmp/output.bin");
        out.write(code);
        out.close();


        // Write it to the disk.
        
    }
}
