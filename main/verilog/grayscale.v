module grayscale (
    input [7:0] r_in,
    input [7:0] g_in,
    input [7:0] b_in,
    output [7:0] r_out,
    output [7:0] g_out,
    output [7:0] b_out
);
    wire [7:0] gray;
    assign gray = (r_in >> 2) + (g_in >> 1) + (b_in >> 2);  // Approximation of 0.25R + 0.5G + 0.25B
    assign r_out = gray;
    assign g_out = gray;
    assign b_out = gray;
endmodule
