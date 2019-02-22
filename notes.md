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


#### 18 Dec 18

* Regarding Frank's new straddle function: what function (fn) do I give as input, LaPlace.solver_t(m, q, is_even) ? Just the shoot_laplace(lam, m, q, is_even) function ?
* Note, the current idea of "multi_rootfind(<args>)" function should be adapted to function with straddle:
  - Need to adapt the "if: ... else: ..." loop to call straddle with the correct parameters, where (fn) is TBD (see ^), (inc)/(fact) should be a <<SMALL>> number & (N_steps) decently large; having it as some fraction of what is currently shift seems reasonable? Or just make N_steps larger if shift is also larger, and choose a fixed inc/fact?
  - The guessed lamlist in the "if: ... else: ..." loop will be the output of straddle.search_log(fn, init_x, fact, N_steps) (init_x should just be the previously found root -- will this work for the first step if I put it bang on the correct value [which is known from Legendre Polynomials ]?)
* In general need to do a restructuring of the code; remove old code (it's on git now so can always recover it), fix commenting style, reorganize function/file structure, fix naming (files should be small letters, Classes with Capitals etc), general sanity checks to be implemented (need to discuss with Frank what are good tests?). Might work on this during Christmas break if I get bored
* Also should note that current method cannot find a point to start with for l=1,0 (k=-1,-2 in Townsend)


