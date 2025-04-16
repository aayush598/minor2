module scale(input [7:0] pixel_in, output reg [7:0] pixel_out);
    reg [7:0] scale_factor;
    
    initial begin
        // Set scaling factor (simple scaling for testing)
        scale_factor = 2;  // Scale by a factor of 2
    end
    
    always @(*) begin
        // Apply scaling (simplified)
        pixel_out = pixel_in * scale_factor;  // Placeholder, actual scaling logic to be added
    end
endmodule
