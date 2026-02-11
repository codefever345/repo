clc;
clear all;
a=3;
b=1;
c1=a*b; %remove the colen for printing
c3=a/b;
c4=a-b;
c5=a\b;

% CREATING MATRIIX

I=eye(2);
z=zeros(4,2)% matrix of 4X2

%row matrix
a1=[1,2,3]
a2=[1,2,3]

%2X2 matrix by using both ways
b1=[1 3; 2 4]
b2=[1,3;2,4]

% Creating a random matrix

R_1=randi([-3,3],2,4) % 2X4 int entris 
R_2=rand(4,2)
m=4;n=5;r=2;
R1=rand(m,r)
R2=rand(r,n)
R_3= ranf(m,r) * rand(r,n)
rank(R_3) % random mat of rank r