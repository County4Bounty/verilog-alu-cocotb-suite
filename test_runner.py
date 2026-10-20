import os
import sys
from pathlib import Path
from cocotb.runner import get_runner

def test_alu_runner():
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent

    sys.path.append(str(proj_path / "tests"))

    runner = get_runner(sim)
    runner.build(
        verilog_sources=[proj_path / "hdl" / "alu.v"],
        hdl_toplevel="alu",
        always=True,
    )
    runner.test(
        hdl_toplevel="alu",
        test_module="test_alu",
    )

if __name__ == "__main__":
    test_alu_runner()