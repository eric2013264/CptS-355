(* Eric Chen 11381898 *)
(* HW5: ML *)

(*********************************************************************************)
(* 1 in_list *********************************************************************)

fun in_list (n, list) =   	(* function in_list *)
  if list = nil then false	(* check for null *)
  else 						
    if hd(list) = n then true	(* if head of list == n *)
    else 
in_list(n, tl(list))		(* recurse tail/rest of list *)

(*********************************************************************************)
(* 2 intersection ****************************************************************)

fun intersection ([],[]) = []
  | intersection (x,[]) = []
  | intersection ([],x) = []
  | intersection ((x::xs),(z)) = if in_list (x,xs) then intersection (xs,z)
    else if in_list (x,z) then x::intersection
    (xs,z) else intersection (xs,z);

(*********************************************************************************)
(* 3 union ***********************************************************************)

fun removeDup(list) = 
  if list = nil then []
  else
    if in_list(hd(list), removeDup(tl(list))) then removeDup(tl(list))
    else hd(list)::removeDup(tl(list))

fun union(list1, list2) = removeDup(list1@list2)  

(*********************************************************************************)
(* 4 filter and reverse **********************************************************)

fun reverse(list) = 
  let 
  fun rev ([], l2) = l2
    | rev (l1, l2) = rev(tl(l1), hd(l1)::l2)
  in
  rev(list, [])
  end

fun filter(fnc, list) = 
  let
  fun accum (f, [], l2) = l2
    | accum (f, l, l2) = 
    if f(hd(l)) then accum(f, tl(l), hd(l)::l2)
    else accum(f, tl(l), l2)
  in
  accum (fnc, reverse(list), [])
  end

(*********************************************************************************)
(* 5 groupNl and groupNr *********************************************************)

fun groupNl(n1, list) = 
  let
  fun grp (n, n2, [], l2, l3) = reverse(l3)::l2
  |   grp (n, n2, l, l2, l3) = 
    if n2 = 0 then grp(n, n, l, reverse(l3)::l2, [])
    else grp (n, n2 - 1, tl(l), l2, hd(l)::l3)
  in
  reverse(grp(n1, n1, list, [], []))
  end

fun groupNr2(n1, list) = 
  let
  fun grp (n, n2, [], l2, l3) = l3::l2
  |   grp (n, n2, l, l2, l3) = 
    if n2 = 0 then grp(n, n, l, l3::l2, [])
    else grp (n, n2 - 1, tl(l), l2, hd(l)::l3)
  in
  reverse(grp(n1, n1, list, [], []))
  end

fun groupNr(n1, list) = reverse(groupNr2(n1, reverse(list)))

(*********************************************************************************)
(* 6 mergesort *******************************************************************)

fun merge([], ys) = ys
  | merge(xs, []) = xs
  | merge(x::xs, y::ys) =
    if x < y then x::merge(xs, y::ys)
    else y::merge(x::xs, ys)

fun split [] = ([],[])
  | split [a] = ([a],[])
  | split (a::b::cs) =
    let val (M,N) = split cs in
      (a::M, b::N)
    end

fun mergesort []  = []
  | mergesort [a] = [a]
  | mergesort [a,b] = if a <= b then [a,b] else [b,a]
  | mergesort L  =
    let val (M,N) = split L
    in
      merge (mergesort M, mergesort N)
    end

(*********************************************************************************)
(* 7 Practice with datatypes *****************************************************)

datatype either = ImAString of string | ImAnInt of int;

datatype eitherTree = LEAF of either | NODE of (eitherTree * eitherTree);

fun eitherSearch (LEAF(ImAnInt x)) y = (x=y)
  | eitherSearch(LEAF(ImAString x)) y = false
  | eitherSearch (NODE (t1,t2)) y = (eitherSearch t1 y)
  orelse (eitherSearch t2 y);

fun eitherTest () =
let
  val L1 = LEAF(ImAnInt 1)
  val L2 = LEAF(ImAnInt 2)
  val L3 = LEAF(ImAnInt 13)
  val L4 = LEAF(ImAnInt 14)
  val L5 = LEAF(ImAnInt 15)
  val L6 = LEAF(ImAString "a")
  val L7 = LEAF(ImAString "b")
  val L8 = LEAF(ImAString "c")
  val L9 = LEAF(ImAString "d")
  val L10 = LEAF(ImAString "e")
  val N1 = NODE (L1,L2)
  val N2 = NODE (N1, L3)
  val N3 = NODE (N2, L4)
  val N4 = NODE (N3, L5)
  val N5 = NODE (N4, L6)
  val N6 = NODE (N5, L7)
  val N7 = NODE (N6, L8)
  val N8 = NODE (N7, L9)
  val N9 = NODE (N8, L10)
    in
      not  (eitherSearch N9 15)
    end;

(*********************************************************************************)
(* 8 treeToString ****************************************************************)

datatype 'a Tree = Empty | LEAF of 'a | NODE of ('a Tree) list;

val L1a = LEAF "a"
val L1b = LEAF "b"
val L1c = LEAF "c"
val L2a = NODE [L1a, L1b, L1c]
val L2b = NODE [L1b, L1c, L1a]
val L3 = NODE [L2a, L2b, L1a, L1b]
val L4 = NODE [L1c, L1b, L3]
val L5 = NODE [L4]
val iL1a = LEAF 1
val iL1b = LEAF 2
val iL1c = LEAF 3
val iL2a = NODE [iL1a, iL1b, iL1c]
val iL2b = NODE [iL1b, iL1c, iL1a]
val iL3 = NODE [iL2a, iL2b, iL1a, iL1b]
val iL4 = NODE [iL1c, iL1b, iL3]
val iL5 = NODE [iL4]

fun treeToString f Node = let
    fun treeFun (Empty) = ["(:"]
    | treeFun (NODE([])) = [")"]
    | treeFun (LEAF(v)) = [f v]
    | treeFun (NODE(h::t)) = [""] @ ( treeFun (h)) @ ( treeFun (NODE(t)) )
    in
    String.concat(treeFun Node)
end;

(*********************************************************************************)
(* 9 Perms ***********************************************************************)

fun insert x [] = [[x]]
  | insert x (y::ys) = let
    fun consy l = y :: l
in (x::y::ys) :: (map consy (insert x ys))
end;

fun perms [] = [[]]
  | perms (x::y) = List.concat (map (insert x) (perms y));
