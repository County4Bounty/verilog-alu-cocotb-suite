`timescale 1ns / 1ps

module alu (
    input  wire        clk,
    input  wire        rst_n,
    input  wire [7:0]  a,
    input  wire [7:0]  b,
    input  wire [2:0]  op,
    output reg  [7:0]  result,
    output wire        zero
);
    // Internal combinational wire for calculation
    reg [7:0] calc_result;

    always @(*) begin
        case (op)
            3'b000: calc_result = a + b;       // ADD
            3'b001: calc_result = a - b;       // SUB
            3'b010: calc_result = a & b;       // AND
            3'b011: calc_result = a | b;       // OR
            3'b100: calc_result = a ^ b;       // XOR
            3'b101: calc_result = a << 1;      // SHL
            default: calc_result = 8'h00;
        endcase
    end

    // Sequential logic: Register the result on the rising clock edge
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            result <= 8'h00;
        end else begin
            result <= calc_result;
        end
    end

    assign zero = (result == 8'h00);
endmodule