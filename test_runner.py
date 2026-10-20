import os
import sys
from pathlib import Path
from cocotb.runner import get_runner

def test_alu_runner():
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent
    tests_dir = proj_path / "tests"

    sys.path.insert(0, str(tests_dir))

    runner = get_runner(sim)
    runner.build(
        verilog_sources=[proj_path / "hdl" / "alu.v"],
        hdl_toplevel="alu",
        always=True,
    )
    runner.test(
        hdl_toplevel="alu",
        test_module="test_alu",
        test_dir=tests_dir,
        python_search=[str(tests_dir)],
    )

if __name__ == "__main__":
    test_alu_runner()