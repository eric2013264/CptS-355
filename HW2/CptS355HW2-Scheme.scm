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


; 2
;; Repl returns a (new) list which is the same as l except that the ith element is v.
;; Index i is assumed to be at least 0 and smaller than the length of the list.
(define (repl listt index value)
    (if (null? listt)     ;; if the list empty?
        listt               ;; if so the length is 0
        (cons               ;; construct
          (if (zero? index) ;; if index == 0
              value           ;; value
              (car listt))    ;; car first item
          (repl (cdr listt) (- index 1) value) ;; list is everything but the first, decrement index
        );cons
    );if
);define

(repl '(1 2 3 4) 1 7)


; 3
;; Range returns a list of ints (min min+1 ... max-1). Return an empty list if min >= max.
(define (range a b)
    (if (>= a b)			;; if a is >= b
        '()				;; if not, return an empty list
        (cons a (range (+ 1 a) b)      ;; recursive step, merge a and range(a+1, b) until a >= b
        );cons
    );if
);define

(range 4 6)

; 4
;; Merge2 merges two lists of integers, each already in ascending order, into a new list that is also in ascending order.
(define (merge2 l1 l2)

  (if (null? l1) l2
      (if (null? l2) l1 ;; if that was the last number, we're done
          (if (<= (car l1) (car l2)) ;; if l1[0] <= l2[0]
          (cons (car l1) (cons (car l2) (merge2 (cdr l1) (cdr l2))))    ;; recursively cons in the right order: l1, l2
          (cons (car l2) (cons (car l1) (merge2 (cdr l1) (cdr l2))))    ;; if l1[0] > l2[0] recursively cons in the right order: l2, l1
          );if
      );if
  );if
);define

(merge2 '(2 4 6) '(1 4 5))

; 5
;; Fold. Given definition of fold in class
(define (fold fcombine basecase L) 
   (cond
      ((null? L) basecase)
      (#t (fcombine (car L) (fold fcombine basecase (cdr L))))
   ))

; 6 
;; mergeN
(define (mergeN listt)
    (cond ((null? listt) listt)
        ((list? (car listt))
        (append (mergeN (car listt))
            (mergeN (cdr listt))))
        (else (cons (car listt)
            (mergeN (cdr listt))))))

(mergeN '((2 4 5) (1 4 6) (3 7 9)))

; 7
;; unzip takes lists as its arguments and produces a pair of lists
;; opposite of the zip function given in class
(define (unzip listt)
    (apply map list listt))

(unzip '((1 2) (3 4) (5 6)))