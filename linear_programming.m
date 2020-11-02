% PRIMENA MATLABA U LINEARNOM PROGRAMIRANJU - Simplex metoda

%ZADATAK 1 - Vezbe 2:
%Odrediti minimum funkcije cilja:

%                      f(x)=-2x1-3x2

%                     x1 + 2x2 <= 6
%                     x1 - x2  <= 4
%                          x2  <=2
%                     x1 , x2  => 0

clc;
clear;
close all;


%----------koriscenjem funkcije linprog() ----------------

f=[-2; -3; 0; 0; 0];
A=zeros(5,5)
b=zeros(5,1)
Aeq=[1 2 1 0 0; 1 -1 0 1 0;0 1 0 0 1;0 0 0 0 0;0 0 0 0 0 ];
beq=[6;4;2;0;0];
lb=[0 ; 0; 0 ; 0 ; 0];
ub=[inf ; inf ;inf ;inf ;inf ];
[X_o,f_x_optimalno] = linprog(f,A,b,Aeq,beq,lb,ub)