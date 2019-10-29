USING: arrays ;
IN: numerical-scratch.sa

! contains the shape and the array values
! shape stored as array (can be any dimension)
TUPLE: matrix { shape array } 
              { vals c-array } ; ! it's mad abt c-array :/