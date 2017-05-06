; first scheme demo

>(+ 4 5)
; 9
>(* 4 5 6)
; 120
>"this is a string"
>#t
; #t
>#f
; #f
>if (#t 1 2)
; 1
>if (#f 1 2)
; 2

>(define x 3)
>x
; 3

>(+ 2 x)
5

; define is not a function; it is a special form

; car "Contents of Address part of Register" 
	; returns first element of list
; cdr "Contents of Decrement part of Register" 
	; returns 2nd and subsequent items in list
; cons "Construct" 
	; takes two arguments and returns a list constructed from those two arguments
