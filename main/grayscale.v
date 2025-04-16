module grayscale(
    input clk,
    input rst,
    input [23:0] rgb_in,    // 8 bits R, G, B
    input valid_in,
    output reg [7:0] gray_out,
    output reg valid_out
);

    reg [7:0] r, g, b;
    reg [15:0] gray_calc;
    
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            r <= 0;
            g <= 0;
            b <= 0;
            gray_out <= 0;
            gray_calc <= 0;
            valid_out <= 0;
        end else if (valid_in) begin
            r <= rgb_in[23:16];
            g <= rgb_in[15:8];
            b <= rgb_in[7:0];
            
            gray_calc <= (r * 77) + (g * 150) + (b * 29);
            gray_out <= gray_calc[15:8]; // Equivalent to >> 8
            valid_out <= 1;
        end else begin
            valid_out <= 0;
        end
    end

endmodule
