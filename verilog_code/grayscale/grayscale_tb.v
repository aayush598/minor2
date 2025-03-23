`timescale 1ns / 1ps
module grayscale_tb;
    reg [7:0] R, G, B;  // RGB input values
    wire [7:0] gray;    // Grayscale output

    // Instantiate the grayscale converter module
    grayscale_converter uut (
        .R(R),
        .G(G),
        .B(B),
        .gray(gray)
    );

    initial begin
        $dumpfile("grayscale_tb.vcd"); // Dump waveform for GTKWave
        $dumpvars(0, grayscale_tb);

        // Test Cases
        R = 8'hFF; G = 8'h00; B = 8'h00; #10;  // Red color
        R = 8'h00; G = 8'hFF; B = 8'h00; #10;  // Green color
        R = 8'h00; G = 8'h00; B = 8'hFF; #10;  // Blue color
        R = 8'h80; G = 8'h80; B = 8'h80; #10;  // Gray color
        R = 8'hFF; G = 8'hFF; B = 8'hFF; #10;  // White color
        R = 8'h00; G = 8'h00; B = 8'h00; #10;  // Black color

        $finish;  // End simulation
    end

    always @(*) begin
        $display("R=%h G=%h B=%h -> Grayscale=%h", R, G, B, gray);
    end

endmodule
