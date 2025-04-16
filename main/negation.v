module negation (
    input [7:0] pixel_in,   // Input pixel value (8-bit grayscale value)
    output reg [7:0] pixel_out // Output negated pixel value
);
    
    // Always block to perform negation operation
    always @(*) begin
        // Negation: Invert the pixel value (255 - pixel_value)
        pixel_out = 255 - pixel_in;
    end

endmodule
