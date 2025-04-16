module grayscale_converter (
    input  [7:0] R,   // Red channel
    input  [7:0] G,   // Green channel
    input  [7:0] B,   // Blue channel
    output [7:0] gray // Grayscale output
);

    reg [15:0] gray_calc; // 16-bit register for intermediate calculation

    always @(*) begin
        gray_calc = (R * 8'd77) + (G * 8'd150) + (B * 8'd29); // Weighted sum
    end

    assign gray = gray_calc[15:8]; // Extract upper 8 bits (division by 256)

endmodule