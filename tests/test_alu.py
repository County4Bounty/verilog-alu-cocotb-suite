import random
import cocotb
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

@cocotb.test()
async def test_alu_sequential(dut):
    """Randomized sequential verification for clocked ALU."""
    
    # 1. Start a 10ns clock (100 MHz) on dut.clk
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # 2. Apply Reset
    dut.rst_n.value = 0
    dut.a.value = 0
    dut.b.value = 0
    dut.op.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.rst_n.value = 1  # Release reset

    # 3. Run 100 randomized clock-cycle test vectors
    for _ in range(100):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        op = random.randint(0, 5)

        dut.a.value = a
        dut.b.value = b
        dut.op.value = op

        # Wait for the next rising clock edge where the ALU samples & registers the output
        await RisingEdge(dut.clk)
        # Wait a tiny delta after the edge for registers to update
        await Timer(1, units="ns")

        # Compute expected result
        if op == 0:   expected = (a + b) & 0xFF
        elif op == 1: expected = (a - b) & 0xFF
        elif op == 2: expected = a & b
        elif op == 3: expected = a | b
        elif op == 4: expected = a ^ b
        elif op == 5: expected = (a << 1) & 0xFF
        else:         expected = 0

        actual_res = int(dut.result.value)
        actual_zero = int(dut.zero.value)
        expected_zero = 1 if expected == 0 else 0

        assert actual_res == expected, f"Mismatch on OP {op}: got {actual_res}, expected {expected}"
        assert actual_zero == expected_zero, "Zero flag failed!"