module flip_horizontal(input [7:0] pixel_in, output reg [7:0] pixel_out);
    always @(*) begin
        // Flip horizontally
        pixel_out = pixel_in;  // Placeholder, actual flip logic to be added
    end
endmodule
