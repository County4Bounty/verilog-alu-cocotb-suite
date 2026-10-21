import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


async def init(dut):
    cocotb.start_soon(Clock(dut.clk, 10, "ns").start())
    dut.a.value = 0
    dut.b.value = 0
    dut.op.value = 0
    dut.rst_n.value = 0
    await Timer(25, "ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)


async def run_op(dut, a, b, op):
    dut.a.value = a
    dut.b.value = b
    dut.op.value = op
    await RisingEdge(dut.clk)
    await Timer(1, "ns")


@cocotb.test()
async def test_add_carry(dut):
    await init(dut)
    await run_op(dut, 0xFF, 0x01, 0b000)
    assert int(dut.result.value) == 0x00
    assert int(dut.carry.value) == 1
    assert int(dut.zero.value) == 1


@cocotb.test()
async def test_sub_borrow_and_negative(dut):
    await init(dut)
    await run_op(dut, 0x00, 0x01, 0b001)
    assert int(dut.result.value) == 0xFF
    assert int(dut.carry.value) == 1
    assert int(dut.negative.value) == 1


@cocotb.test()
async def test_shr_and_not(dut):
    await init(dut)
    await run_op(dut, 0b00000011, 0, 0b110)
    assert int(dut.result.value) == 0b00000001
    assert int(dut.carry.value) == 1
    await run_op(dut, 0x0F, 0, 0b111)
    assert int(dut.result.value) == 0xF0


@cocotb.test()
async def test_reset_clears_outputs(dut):
    await init(dut)
    await run_op(dut, 0xFF, 0x01, 0b000)
    dut.rst_n.value = 0
    await Timer(2, "ns")
    assert int(dut.result.value) == 0
    assert int(dut.carry.value) == 0