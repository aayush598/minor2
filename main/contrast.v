module contrast (
    input [7:0] r_in,
    input [7:0] g_in,
    input [7:0] b_in,
    output [7:0] r_out,
    output [7:0] g_out,
    output [7:0] b_out
);
    parameter CONTRAST = 1.01;  // Contrast factor (1.0 = no change, >1 = increase contrast)

    wire [7:0] r_contrast, g_contrast, b_contrast;

    assign r_contrast = (r_in - 128) * CONTRAST + 128;
    assign g_contrast = (g_in - 128) * CONTRAST + 128;
    assign b_contrast = (b_in - 128) * CONTRAST + 128;

    assign r_out = (r_contrast > 255) ? 8'd255 : (r_contrast < 0) ? 8'd0 : r_contrast;
    assign g_out = (g_contrast > 255) ? 8'd255 : (g_contrast < 0) ? 8'd0 : g_contrast;
    assign b_out = (b_contrast > 255) ? 8'd255 : (b_contrast < 0) ? 8'd0 : b_contrast;
endmodule
