function  resiz4(im, a)
    figure;
    imshow(im)

    in_rows = size(im,1);
    in_cols = size(im,2);
    out_rows = round( a*in_rows);
    out_cols = round(a*in_cols);

    
    S_R = in_rows / out_rows;

    S_C = in_cols / out_cols;


    [cf, rf] = meshgrid(1 : out_cols, 1 : out_rows);

    rf = rf * S_R;
    cf = cf * S_C;


    r = floor(rf);
    c = floor(cf);

    r(r < 1) = 1;
    c(c < 1) = 1;
    r(r > in_rows - 1) = in_rows - 1;
    c(c > in_cols - 1) = in_cols - 1;


    delta_R = rf - r;
    delta_C = cf - c;


    in1_ind = sub2ind([in_rows, in_cols], r, c);
    in2_ind = sub2ind([in_rows, in_cols], r+1,c);
    in3_ind = sub2ind([in_rows, in_cols], r, c+1);
    in4_ind = sub2ind([in_rows, in_cols], r+1, c+1);       

 
    out = zeros(out_rows, out_cols, size(im, 3));
    out = cast(out, class(im));

    for idx = 1 : size(im, 3)
        chan = double(im(:,:,idx));
        tmp = chan(in1_ind).*(1 - delta_R).*(1 - delta_C) + ...
                       chan(in2_ind).*(delta_R).*(1 - delta_C) + ...
                       chan(in3_ind).*(1 - delta_R).*(delta_C) + ...
                       chan(in4_ind).*(delta_R).*(delta_C);
        out(:,:,idx) = cast(tmp, class(im));
    end
    figure;
    imshow(out)
    imwrite(out,'conan_resiz1.png');