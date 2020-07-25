% DANH TRI HIEU DEP TRAI 
%--------------------------------------

function dca

clc;             %xoa man hinh
syms x y;
%B1: t?o ma tr?n
a=input('nhap ma tran:');
[m,n]=size(a);  
may=[1:n];
a = [may;a];
chitiet= [0:m];
chitiet =chitiet'; 
a= [chitiet a(:,1:n)];
disp('ma tran la:');
disp(a);

%B2: tính t?ng hàng c?t
disp('tong hang cot ma tran la:');
[m,n] = size(a);
z=0;
k=0;

%t?ng các c?t
for i=2:1:n 
    for j=2:1:m
        z = z + a(j,i);
    end
    k(i-1) = z;
    z=0;
end
disp('tong cot la: ');
disp(k);
%t?ng các hàng 
for i=2:1:m 
    for j=2:1:n
        z = z + a(i,j);
    end
    p(i-1) = z;
    z=0;
end
disp('tong hang la: ')
disp(p);

%s?p x?p
k = [0 k(:,1:n-1)];
p = [0 p(:,1:m-1)];
p = [p(:,1:m) 0];
a = [a;k];
p=p';
a=[a(:,1:n) p];
disp('ma tran a sau khi tinh tong hang cot la: ')
disp(a);


[m,n] = size(a);
k = a(m,2:n-1);
disp(k);
p = a(2:m-1,n);
disp(p);

% B3: sap xep hang theo thu tu giam dan 
for i=2:1:m-2
    for j= i:1:m-1
        if (a(i,n) < a(j,n))
            ptemp = a(i,:);
            a(i,:) = a(j,:);
            a(j,:) = ptemp;
        end
    end
end 
disp(a);


% B4: sap xep cot theo thu tu tang dan 
for i=2:1:n-2
    for j= i:1:n-1
        if (a(m,i) > a(m,j))
            ptemp = a(:,i);
            a(:,i) = a(:,j);
            a(:,j) = ptemp;
        end
    end
end
disp(a);

%B5: sap xep cot theo (hang dau co 1 sang trai)
z=2; % vi tri cac cot da duoc sap xep
for i=2:1:m-1   %duyet tat ca cac hang
    % don 1 sang trai
    for j= z:1:n-2
        for o= j:1:n-1
            if ((a(i,j) == 0) && (a(i,o) == 1) )
                ptemp = a(:,j);
                a(:,j) = a(:,o);
                a(:,o) = ptemp;
                z=j+1; %
                break;
            end
        end
    end
    disp(a);
end
disp('ma tran sau khi don 1 sang trai la:');
disp(a);

%B6: sap xep hang theo (cot dau co 1 len tren)
z=2; % vi tri cac hang da duoc sap xep
for i=2:1:n-1   %duyet tat ca cac cot
    % don 1 len tren
    for j= z:1:m-2
        for o= j:1:m-1
            if ((a(j,i) == 0) && (a(o,i) == 1) )
                ptemp = a(j,:);
                a(j,:) = a(o,:);
                a(o,:) = ptemp;
                if(j == 2)
                    z = j;
                else
                    z=j+1;
                break;
            end
        end
    end
end
disp('ma tran sau khi don 1 len tren la:');
disp(a);
end