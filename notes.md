#### 4 Sep 18

* SURFdrive, check secretariat
* Dropbox with stuff
* Goal before christmas; figure 1 plot from Townsend03
    - Basic concept knowledge for intro (eg what is a burst)
* Visualize the problem (rotating sphere with small patch rotating slightly differently)

* for intro; density/physical depth/coumn depth difference should be discussed


#### 20 Sep 18

* Reading on asymptotic limits
    - General methods for solving differential equations every now and then
    - When are tehy valid/when can you throw them away
* Abramowitz and Stegun: Handbook of Mathematical Functions (reference book for functions)


#### 26 Sep 18

* Book is a different book than ^, as that does not contain asymptotic functions/solutions


#### Mathematica code
For Townsend 2003 eq 40/41 solutions on the s=0 case:

(*lambda- *)FullSimplify[a^2 - a q + 0.5 q^2 (1 - Sqrt[1 - (4 (-a^2 + a q))/q^2]), Element[a | q, Reals]]

(*lambda+ *)FullSimplify[a^2 - a q + 0.5 q^2 (1 + Sqrt[1 - (4 (-a^2 + a q))/q^2]), Element[a | q, Reals]]


#### 22 Oct 18

* Get into numerics
* First Legendre polynomials: (reminder m<=l)
    - m=1, l=1,2,3
    - m=2, l=2,3,4
    - m=3, l=3,4,5
    - m=4, l=4,5,6
    - m=5, l=5,6,7


#### 1 Nov 18

* Need to rewrite setup for ODE with eigenvalue
