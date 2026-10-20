# 8-bit Sequential ALU & Automated Verification Suite

[![Verification Pipeline](https://github.com/County4Bounty/verilog-alu-cocotb-suite/actions/workflows/ci.yml/badge.svg)](https://github.com/County4Bounty/verilog-alu-cocotb-suite/actions)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Verilog](https://img.shields.io/badge/Verilog-IEEE_1364-orange.svg)
![Cocotb](https://img.shields.io/badge/Verification-Cocotb-green.svg)

An industry-grade, open-source hardware design and verification project implementing a clocked 8-bit Arithmetic Logic Unit (ALU) in **Verilog**, verified using a modern Python-based co-simulation framework (**Cocotb**), and automated with a **GitHub Actions CI/CD pipeline**.

---

## Architecture & Features

### 1. Sequential Hardware Design (`hdl/alu.v`)
- **Clocked Pipeline:** Features active-low asynchronous reset (`rst_n`) and synchronous edge-triggered registers (`clk`) for realistic RTL design practices.
- **Operations Supported:**
  - Arithmetic: Addition (`+`), Subtraction (`-`)
  - Bitwise Logic: AND (`&`), OR (`|`), XOR (`^`)
  - Shifts: Logical Shift Left (`<< 1`)
- **Status Flags:** Zero flag generation (`zero`) asserted when output registers evaluate to `8'h00`.

### 2. Python-Driven Functional Verification (`tests/test_alu.py`)
- **Randomized Constrained Stimulus:** Generates 100% randomized test vectors across inputs and operation selectors.
- **Cocotb Co-Simulation:** Drives synchronous clock generation (`cocotb.clock.Clock`), samples rising edges (`RisingEdge`), and automatically asserts correctness against expected software models.

### 3. Automated CI/CD Pipeline (`.github/workflows/ci.yml`)
- Automatically provisions an Ubuntu virtual machine on every commit.
- Installs `Icarus Verilog` and Python dependencies (`cocotb`, `pytest`).
- Executes the test runner (`test_runner.py`) and reports build status via live badges.

---

## Repository Structure

```text
verilog-alu-cocotb-suite/
├── .github/
│   └── workflows/
│       └── ci.yml          # Automated CI/CD test runner
├── hdl/
│   └── alu.v               # Sequential Verilog ALU RTL
├── tests/
│   └── test_alu.py         # Cocotb Python randomized testbench
├── test_runner.py          # Native Python test runner entrypoint
└── README.md               # Project documentation