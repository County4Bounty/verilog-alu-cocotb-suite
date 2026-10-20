import random
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_alu_randomized(dut):
    """Randomized verification for 8-bit ALU operations."""
    dut.a.value = 0
    dut.b.value = 0
    dut.op.value = 0
    await Timer(1, units="ns")

    for _ in range(100):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        op = random.randint(0, 5)

        dut.a.value = a
        dut.b.value = b
        dut.op.value = op
        await Timer(1, units="ns")

        if op == 0:
            expected = (a + b) & 0xFF
        elif op == 1:
            expected = (a - b) & 0xFF
        elif op == 2:
            expected = a & b
        elif op == 3:
            expected = a | b
        elif op == 4:
            expected = a ^ b
        elif op == 5:
            expected = (a << 1) & 0xFF
        else:
            expected = 0

        actual_res = int(dut.result.value)
        actual_zero = int(dut.zero.value)
        expected_zero = 1 if expected == 0 else 0

        assert actual_res == expected, f"Mismatch on OP {op}: got {actual_res}, expected {expected}"
        assert actual_zero == expected_zero, "Zero flag failed!"