`timescale 1ns / 1ps
module tb_flip_horizontal;

    reg [7:0] r_in, g_in, b_in;
    wire [7:0] r_out, g_out, b_out;

    integer infile, outfile, r;
    integer width, height, row, col;
    reg [23:0] row_pixels[0:4095]; // Increase if image width > 4096

    flip_horizontal uut (
        .r_in(r_in), .g_in(g_in), .b_in(b_in),
        .r_out(r_out), .g_out(g_out), .b_out(b_out)
    );

    initial begin
        // Load width & height
        $readmemh("output/input_width.txt", row_pixels, 0, 0);
        width = row_pixels[0];
        $readmemh("output/input_height.txt", row_pixels, 0, 0);
        height = row_pixels[0];

        infile = $fopen("output/input.hex", "r");
        outfile = $fopen("output/processed.hex", "w");

        if (infile == 0 || outfile == 0) begin
            $display("❌ Error opening file.");
            $finish;
        end

        for (row = 0; row < height; row = row + 1) begin
            // Read one row of pixels
            for (col = 0; col < width; col = col + 1) begin
                r = $fscanf(infile, "%2x%2x%2x", r_in, g_in, b_in);
                #1;
                row_pixels[col] = {r_out, g_out, b_out};
            end

            // Write the row in reverse (horizontal flip)
            for (col = width - 1; col >= 0; col = col - 1) begin
                $fwrite(outfile, "%02x%02x%02x", row_pixels[col][23:16], row_pixels[col][15:8], row_pixels[col][7:0]);
            end
        end

        $fclose(infile);
        $fclose(outfile);
        $finish;
    end
endmodule
