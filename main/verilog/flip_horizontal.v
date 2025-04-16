module flip_horizontal (
    input [7:0] r_in,
    input [7:0] g_in,
    input [7:0] b_in,
    output [7:0] r_out,
    output [7:0] g_out,
    output [7:0] b_out
);
    assign r_out = r_in;
    assign g_out = g_in;
    assign b_out = b_in;
endmodule
