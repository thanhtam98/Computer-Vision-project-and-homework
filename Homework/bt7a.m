function bt7a
img = imread('bt7.jpg');
gray = rgb2gray(img);
binary = imbinarize(gray,graythresh(gray));
nbinary = ~binary;
gray2 = imfill(nbinary,'holes');
%gray3 = imopen(gray2,ones(3,3));
gray4 = bwareaopen(gray2,1);
%imshow(gray2)
gray_perim = bwperim(gray4);
overlay1 = imoverlay(gray, gray_perim, [.3 1 .3]);
CC = bwconncomp(gray_perim);
Ilabel = logical(gray2);
stat = regionprops(Ilabel,'centroid');

location = zeros(numel(stat),2);
for x = 1: numel(stat)
    location(x,1) = stat(x).Centroid(1);
    location(x,2) = stat(x).Centroid(2);
end
numel(stat)
figure;
imshow(overlay1)

a = CC.NumObjects;

[idx,C] = kmeans(location,6);
num = zeros(6,1);
for i = 1:numel(stat)
    num(idx(i,1),1) = num(idx(i,1),1)+1;
end
num
for i = 1:6
   caption = sprintf('%d', num(i,1));
   text(C(i,1)-15,C(i,2)-15 , caption, 'FontSize', 30,'Color','r'); 
end

caption = sprintf('tong so cham = %d', a);
text(10, 10, caption, 'FontSize', 30,'Color','r');

