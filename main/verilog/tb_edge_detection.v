`timescale 1ns / 1ps
module tb_edge_detection;

    reg [7:0] img[0:65535];
    integer width = 256;
    integer height = 256;
    integer infile, outfile, i, j, idx;

    reg [7:0] p00, p01, p02, p10, p11, p12, p20, p21, p22;
    wire [7:0] edge;

    edge_detection ed (
        .p00(p00), .p01(p01), .p02(p02),
        .p10(p10), .p11(p11), .p12(p12),
        .p20(p20), .p21(p21), .p22(p22),
        .edge(edge)
    );

    initial begin
        infile = $fopen("output/input.hex", "r");
        outfile = $fopen("output/processed.hex", "w");

        if (infile == 0 || outfile == 0) begin
            $display("File open error!");
            $finish;
        end

        // Read grayscale image
        for (i = 0; i < height; i = i + 1) begin
            for (j = 0; j < width; j = j + 1) begin
                $fscanf(infile, "%2x", img[i * width + j]);
            end
        end

        // Apply edge detection (skip borders)
        for (i = 1; i < height - 1; i = i + 1) begin
            for (j = 1; j < width - 1; j = j + 1) begin
                p00 = img[(i - 1) * width + (j - 1)];
                p01 = img[(i - 1) * width + j];
                p02 = img[(i - 1) * width + (j + 1)];

                p10 = img[i * width + (j - 1)];
                p11 = img[i * width + j];
                p12 = img[i * width + (j + 1)];

                p20 = img[(i + 1) * width + (j - 1)];
                p21 = img[(i + 1) * width + j];
                p22 = img[(i + 1) * width + (j + 1)];

                #1;
                $fwrite(outfile, "%02x%02x%02x", edge, edge, edge);
            end
            // Fill border pixel with black
            $fwrite(outfile, "%02x%02x%02x", 8'd0, 8'd0, 8'd0);  // end of row pixel
        end

        $fclose(infile);
        $fclose(outfile);
        $finish;
    end
endmodule
