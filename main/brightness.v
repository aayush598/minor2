module brightness (
    input [7:0] r_in,
    input [7:0] g_in,
    input [7:0] b_in,
    output [7:0] r_out,
    output [7:0] g_out,
    output [7:0] b_out
);
    parameter BRIGHTNESS = 50; // Increase value, range: 0-255

    assign r_out = (r_in + BRIGHTNESS > 255) ? 8'd255 : r_in + BRIGHTNESS;
    assign g_out = (g_in + BRIGHTNESS > 255) ? 8'd255 : g_in + BRIGHTNESS;
    assign b_out = (b_in + BRIGHTNESS > 255) ? 8'd255 : b_in + BRIGHTNESS;
endmodule
