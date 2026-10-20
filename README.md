# 8-bit ALU Design & Cocotb Verification Suite

[![Verification Pipeline](https://github.com/County4Bounty/verilog-alu-cocotb-suite/actions/workflows/ci.yml/badge.svg)](https://github.com/County4Bounty/verilog-alu-cocotb-suite/actions)

An open-source 8-bit Arithmetic Logic Unit (ALU) implemented in Verilog and verified using a coroutine-based Python co-simulation framework (**Cocotb**).

## Features
- **Design:** Combinational 8-bit ALU supporting Arithmetic (ADD, SUB), Logic (AND, OR, XOR), and Shift operations.
- **Verification:** 100% randomized test vectors executed via `cocotb` and `Icarus Verilog`.
- **CI/CD:** Automated verification on every commit via GitHub Actions.