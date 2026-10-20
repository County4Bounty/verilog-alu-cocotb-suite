`timescale 1ns / 1ps

module alu (
    input  wire [7:0] a,
    input  wire [7:0] b,
    input  wire [2:0] op,
    output reg  [7:0] result,
    output wire       zero
);
    always @(*) begin
        case (op)
            3'b000: result = a + b;       // ADD
            3'b001: result = a - b;       // SUB
            3'b010: result = a & b;       // AND
            3'b011: result = a | b;       // OR
            3'b100: result = a ^ b;       // XOR
            3'b101: result = a << 1;      // SHL
            default: result = 8'h00;
        endcase
    end

    assign zero = (result == 8'h00);
endmodule