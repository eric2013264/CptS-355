;; Eric Chen 11381898
;; CptS 355 HW 2 - Scheme

; 1
;; nth returns the nth element of a list (0-based indexing).
(define (nth listt index)
    (if (null? listt)     ;; is the list empty? 
        0                 ;; if so the length is 0
        (if (zero? index) ;; if index == 0
           (car listt)   ;; car first item
            (nth (cdr listt) (- index 1))  ;; cdr list, decrement index
        );if
    );if
);define

(nth '(1 2 3 4) 1)

;;; please email me to reference the rest of my work.