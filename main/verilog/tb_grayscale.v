`timescale 1ns / 1ps
module tb_grayscale;
    reg [7:0] r_in, g_in, b_in;
    wire [7:0] r_out, g_out, b_out;

    integer infile, outfile, r;
    reg [23:0] pixel;

    grayscale uut (
        .r_in(r_in), .g_in(g_in), .b_in(b_in),
        .r_out(r_out), .g_out(g_out), .b_out(b_out)
    );

    initial begin
        infile = $fopen("output/input.hex", "r");
        outfile = $fopen("output/processed.hex", "w");

        if (infile == 0 || outfile == 0) begin
            $display("Failed to open file.");
            $finish;
        end

        while (!$feof(infile)) begin
            r = $fscanf(infile, "%2x%2x%2x", r_in, g_in, b_in);
            #1;
            $fwrite(outfile, "%02x%02x%02x", r_out, g_out, b_out);
        end

        $fclose(infile);
        $fclose(outfile);
        $finish;
    end
endmodule
