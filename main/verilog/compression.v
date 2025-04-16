module compression(input [7:0] pixel_in, output reg [7:0] pixel_out);
    always @(*) begin
        // Apply compression (simplified)
        pixel_out = pixel_in >> 1;  // Simulate compression by reducing precision
    end
endmodule
