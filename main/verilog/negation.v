module negation (
    input [7:0] r_in,
    input [7:0] g_in,
    input [7:0] b_in,
    output [7:0] r_out,
    output [7:0] g_out,
    output [7:0] b_out
);
    assign r_out = 8'd255 - r_in;
    assign g_out = 8'd255 - g_in;
    assign b_out = 8'd255 - b_in;
endmodule
