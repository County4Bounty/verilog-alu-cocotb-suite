`timescale 1ns / 1ps

module alu (
    input  wire        clk,
    input  wire        rst_n,
    input  wire [7:0]  a,
    input  wire [7:0]  b,
    input  wire [2:0]  op,
    output reg  [7:0]  result,
    output reg         carry,
    output wire        zero,
    output wire        negative
);
    // 9-bit combinational result: bit 8 is carry/borrow/shifted-out bit
    reg [8:0] calc;

    always @(*) begin
        case (op)
            3'b000: calc = {1'b0, a} + {1'b0, b};   // ADD
            3'b001: calc = {1'b0, a} - {1'b0, b};   // SUB (bit 8 = borrow)
            3'b010: calc = {1'b0, a & b};           // AND
            3'b011: calc = {1'b0, a | b};           // OR
            3'b100: calc = {1'b0, a ^ b};           // XOR
            3'b101: calc = {a[7], a[6:0], 1'b0};    // SHL (carry = bit shifted out)
            3'b110: calc = {a[0], 1'b0, a[7:1]};    // SHR (carry = bit shifted out)
            3'b111: calc = {1'b0, ~a};              // NOT
            default: calc = 9'h000;
        endcase
    end

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            result <= 8'h00;
            carry  <= 1'b0;
        end else begin
            result <= calc[7:0];
            carry  <= calc[8];
        end
    end

    assign zero     = (result == 8'h00);
    assign negative = result[7];
endmodule