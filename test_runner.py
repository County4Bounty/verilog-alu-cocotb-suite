import os
import sys
from pathlib import Path

# Support both older Cocotb 1.x and the new Cocotb 2.x directory structures
try:
    from cocotb.runner import get_runner
except ImportError:
    from cocotb_tools.runner import get_runner

def test_alu_runner():
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent
    tests_dir = proj_path / "tests"

    # Explicitly ensure child simulation processes can find test_alu.py
    sys.path.insert(0, str(tests_dir))
    os.environ["PYTHONPATH"] = str(tests_dir) + os.pathsep + os.environ.get("PYTHONPATH", "")

    runner = get_runner(sim)
    runner.build(
        verilog_sources=[proj_path / "hdl" / "alu.v"],
        hdl_toplevel="alu",
        always=True,
    )
    runner.test(
        hdl_toplevel="alu",
        test_module="test_alu"
    )

if __name__ == "__main__":
    test_alu_runner()