**NOTE**, sentences surrounded by ?'s (?like this?) are questions **I** have

# Papers

### Thermonuclear Burning on Rapidly Accreting Neutron Stars, Bildsten 1998
* Thermal stability and nuclear ignition depend on the accretion rate **per unit area**
    - Hence this defines **local** behavior on the neutron star and it can differ between spots on the star
    - ?Does this mean that if the accretion happens at different latitudes, due to different "rotational smearing" this can already change?
    - Magnetic fields can change the accretion location
* If the helium ignites before all the hydrogen has been burned, there will be more C to be used in the hydrogen-burning CNO cycle -> ?does that mean that the surface burning increases over time?
    - ?Can it even prevent bursts from happening at all, instead keeping a steady state of burning?
* ?**All** nuclear burning is thin shell burning, on the neutron star surface?
* The outcome of an unstable helium flash depends on the neutron star *radius* and *mass* - ?which might be linked in a general NS EoS?
    - **NOTE** find where this is mentioned again, end of Ch2, start of Ch3?
* In one dimension (?radial component?), the system will always evolve into a cycle, gathering fuel for a time before eventually a thermal instability is reached which can be observed
    - ?This one-dimensionality is about the spread of the fuel accros the NS, not the shape of the NS itself? Ch5 expands on this a bit
    - See **Table 1** for a detailed overview, on page 17
    - These conditions can be broken, see Ch3.3 


### The Rapid Proton Process Ashes from Stable Nuclear Burning on an Accreting Neutron Star, Schatz, Bildsten & Cumming 1999
* H/He burning is thermally stable at high accretion rates (M_dot > 1e-8 M_sol/year)
* The composition of an accreted/accreting NS ocean and crust is very different from the primordial one, due to electron captures, neutron emissions and pycnonuclear (nuclear reactions caused by the density) reactions which release energy locally and drive the matter neutron rich
    - As the H burning of these rapidly accreting NS goes via the rapid proton (rp, Wallace & Woosley 1981) process, a complicated mix of elements is created, nearly all of them heavier than iron
* Used an rp-network that included 631 nuclei between hydrogen and ¹⁰⁰Sn
    - It covers the range of stability to the **proton drip line** (nuclear decay that emits protons)
    - All proton-, neutron-, and \alpha-induced reactions as well as photodisintegration, \beta⁺ decay and electron capture are considered
* For the EoS, it was assumed the ions behave as an ideal gas because Coulomb corrections to the ion EoS is unimportant at the column depths of interest
* When burning is thermally stable, He is consumed within 20 minutes which enhances the number of CNO seed nuclei and when coupled with the breakout from the CNO cycle it leads to a rapid consumption of H through the rp-process
* For all accretion rates where the burning is in a steady state, consumption of H by the CNO cycle is **not** important before He ignition, the He ignition acts as the trigger for H burning
    - For these accretion rates this high (stable burning has M_dot > 1e-8 M_sol/year), the *depth for the CNO cycle is much greater than the depth for He burning*, so He ignites before a significant portion of H has been burned
    - This is still true when considering breakouts from the hot CNO cycle
* The strong temperature sensitivity of the (\alpha, p) reactions (eg ¹⁴O(\alpha, p)¹⁷F) in the \alpha p process is imprinted on the rp-process ashes
    - In addition, some of these nuclear processes are more sensitive to single proton captures than others, or follow 2p capture reactions (eg ²²Mg <-> ²³Al are in (p, \gamma) <-> (\gamma, p) balance, but ²³Al(p, \gamma)²⁴Si creates a flow from ²²Mg to ²⁴Si) - >nuclear stuff is complex<
* ?How realistic/physical are the 1, 5, 20 and 50 m_dot models? -- They're superEddington, and also the rates needed to reach stable burning
* ?They used stable burning calculations to find out what happens to the remnants of the accreted, burned material at higher densities - how much of this is applicable for unstable burning? -- Very little applies to unstable burning, mostly an example of how nuclear physics get involved
* ?Stable =/= continuus burning? (Fig 4, drop in H abundance) ?Or did they compare a "flash frame setup" decay? -- Probably followed a "package" down into the NS


### Asymptotic expressions for the angular dependence of low-frequency pulsation modes in rotating stars, Townsend 2003
* ?How low frequency is "low-frequency"? -- See if this is mentioned eventually in this paper or one of the older ones, it *should* be discussed at some point - once we know what it is can check if my solutions are in this low limit (or a high limit should that come to pass)
    - Low-frequency pulsation modes does **not** mean the star is slowly rotating per se
* ?Condition for the star to be rotating with angular velocity (\Omega) which is uniform, but aren't NS rotating differentially? -- helps make the math nicer, but we're aware that they are (most likely) differentially rotating
* ?To be sure - "equatorial" waves means they are 'stuck' on the equator right? -- Equatorial waves are waves confined to latitudes around the equator, some are more confined than others but in general they dampen out if they go too far from the equator
* The traditional approximation permits the separation of the pulsation equations in all three spherical-polar coordinates (r, \theta, \phi) under the conditions:
    - Star is rotating with *uniform* angular velocity **\Omega**, *with* a neglected horizontal component when evaulating the inertial Coriolis force in the linearized momentum equations - this is valid when \Omega \equiv |**\Omega**| and \omega (pulsation angular frequency) in the corotating frame is significantly smaller than the Brunt-Väisälä frequency N
    - \Omega << (GM/R³)^.5 - centrifugal distortion of the quiescent star may be neglected (?Can bursting NS be considered quiescent?)
    - Perturbations to specific entropy can be neglected (adiabatic approximation)
    - Perturbations to the gravitation potential may be neglected (Cowling 1941 approximation)
    - The neglected horizontal component mentioned above is what is called "the traditional approxtimation" - see Lee&Saio 1997 for math behind this approximation
* For the separated pulsation equations:
    - The azimuthal (\phi) dependence of modes is the same as in the case without rotation (and trivial to solve)
    - The polar (\theta) dependence is governed by Laplace's tidal equations. The eigensolutions are named after their originator Hough (1898)
    - the Hough functions constitute a one-parameter family in the "spin parameter" \nu \equiv 2\Omega/\omega. These are associated with an eigenvalue \lambda which is related to the effective horizontal wavenumber k_\perp of the pulsation via (k_\perp)²=\lambda/(r²). *Note* that negative values of \lambda **can** arise but they are not considered for this paper
* General values of the spin parameter \nu force a numerical approach to solving Laplace's equations. However, approximate analytical solutions can be obtained which become exact in the asymptotic limit of large |\nu|
* The paper specifically goes into the analytical, asymptotic limit |\nu| >> 1 demonstration to solve the tidal equations (eq 18, 21, 22), and will only retain those with the proper boundary conditions
    - So for modes with m=/=0 (non-asisymmetric) this requires the solutions to decay towards zero as |\mu|->1 is approached to ensure (as much as possible) single values of the general solutions (eq8-12) at the stellar poles
    - For axisymmetric modes, the same decay requirement is applied for the polar gradient of the solutions so the general solutions at the poles maintain smoothness
* For larger values of |\nu|, the Hough functions remain close to zero outside of the interval |\mu| <~ |\nu|^-1 (so for larger |\nu|, Hough functions are zero except for smaller |\mu|)
    - Yoshida (1959) started the idea of a Coriolis-force originated 'equatorial waveguide' which prevents low-frequency waves from propagating towards high latitudes and thus traps low-frequency waves in the equatorial area
    - Large |\nu| can be achieved through large values of |**\Omega**| (angular velocity), or through small values of \omega, the angular frequency in the corotating frame. ?Note that the traditional approximation used requires both to be *significantly* smaller than the Brunt-Väisälä frequency N, so only the latter option will work, or is N some huge value? Does that mean that the low-frequency modes have to move around the star slowly (or at least slowly compared to the angular velocity or N)?
* Small \mu leads to neglection of terms \sim \mu², so \mathcal{D} reduces to approximately \frac{d}{d\mu}
    - Note that in eq22 it only dissapears when \lambda =/= \mu²
* Eq 30 has a (close) resemblance to the time-independent Schrödinger equation for a quantum harmonic oscillator, which also describes a wave propagation within a quadratic potential well. The solution for Eq 30 under the set boundary conditions can only be achieved if S = 2s + 1, with s >= 0 as an integer of 'meridional order' - ?What is a meridional "order" specifically?
    - Meridional means "along a longitudinal circle "(aka north-south direction)
    - ?For vector fields the meridional component is the y-component (denoted as v typically) so how exactly should I look at this here?
* The solutions to eq 30 are made with the "Hermite polynomials", but specifically the physicist ones. Have checked for the first two (where s=0, 1) and they are indeed correct.
    - ?How much prove do I need to show that they are solutions ~~/ *how* do I show it, or can I skip that in my thesis (and just say "as noted by e.g. Townsend 2003, they are solutions")?~~ Can show it through the derivative relation H_n'(x) = 2xH_n(x) - H_n+1(x)
* ?The two eigenvalue branches are associated with the gmode/rmode respectively because of the way the functions depend on \nu - with the +branch going as \nu² while the -branch goes as \nu^0 to highest order, so compare with Pedlosky F3.10.1 (p83) to see the relation to the common waves?
    - ?Since for NS the burning layer can be seen as "shallow water" approximation, or would this be true even if that approximation broke?
* The mixed r-mode/g-mode character of \lambda is called "Yanai mode" in this paper (other papers might refer to it as "mixed gravity-Rossby waves")
* Do note that the paper for Eq44 is wrong; it should be \mu_½ \sim ((2s+1)²/(m\nu-m²))^½ (the 2s+1 term is not squared in the paper)
    - In the section following this equation, they also mistakenly list the r-mode solutions validity; it should hold when m\nu >~ (2s+1)²+m² -- Note that in Figure1 it looks like they did implement the correct version, since it cuts off at ~\nu=-6 (and m=-2)
* Lee&Saio1997 have shown that in the non-rotating limit, the \Theta Hough functions for all prograde modes and retrograde g-modes reduce to associated Legendre functions P^m_l where m is the usual azimuthal order and the integer l >= 0 is the harmonic degree
    - ?Harmonic degree?
    - However, this scheme does not include r modes nor retrograde Yanai modes, so Lee&Saio devised an alternative scheme which centers around the assignment of a unique integer index k
    - For positive or zero k, a counterpart exists of harmonic degree l = |m| + k for the non-rotating limit
    - For negative k, it relates to r modes and Yanai modes, or (for \lambda less than 0) convective modes which are neglected in this work
    - This indexing of solutions with k is determined by the requirement that the eigenvalues \lambda_k *at every m and \nu* fall into the sequence \lambda_k+1 > \lambda_k. This is possible because the eigenvalues of the tidal equations are **guaranteed** to never be degenerate (Townsend1997a,b)
* Can relate the meridional order s of the solutions easily to the k index
    - Prograde modes: s = k - 1 (g-mode, Yanai mode and Kelvin mode)
    - Retrograde modes: s = -k - 1 if r-mode, s = k + 1 if g-mode (both formula here work for Yanai mode)
    - This means that the k-based indexing is capable of identifying all modes uniquely (unlike the s-indexing), see also Table1

* !Math questions below!
* ~~?Eq 17 in the paper has minus signs on the LHS; I do not have any minus signs in my version of eq17, but I do get the matching Y_\perp:Y_p equation (14)? -- ??Checked with Frank he also doesn't get the - signs, and when checking with Bildsten 1996 paper to recover L_\mu=-\lambda (eq6 for L_\mu) it looks like I need the - signs to get it to work??~~
    - ~~?Eq 18 **is** correct when following Townsend2003, and I can recover the L_\mu=-\lambda equation (plus an extra term? but still got the other 3 correctly...) so what are we missing on the eq17 minus signs?~~
    - **SOLVED**; the issue was that a minus sign was missing in the middle term of eq20, which would flip the sign on eq17 correctly (and does indeed result in the correct signs for eq19 which otherwise also would've had that issue, but is now correct)
* ?Can reproduce eq15/19 without the lambda too - why does it come in **here** and not somewhere else? Specifically because this is the continuity equation? -- Technically supposed to put it in for 14/17 and 14/18 too, but try and put in "\alpha" and add "\beta" instead of \lambda and the functions of \alpha and \beta are coupled so that you can set \alpha/alpha = 1 and \beta/\alpha = \lambda and thus only have one parameter


### Thermonuclear Burst Oscillations, Anna Watts 2012
* Are all burst oscillators ms pulsars? Is that selection/data bias?
  - They are not; initially people thought that "bursters don't pulse, and pulsars don't burst"
* "Sources with burst oscillations frequency <400 Hz tend to have short, most likely helium-dominated bursts". <> Didn't we discuss this in the last group meeting that there seems to be a limit at 401Hz, which if this is true could be due to the fact that they are He bursters? Would explain the plateau'ing of sources (as to why its 400, dunno)
* PRE = Photospheric Radius Expansion
* ?Burst Oscillation Trains?


### The shallow-water equations in non-spherical geometry with latitudinal variation of gravity, Staniforth & White 2014
* Non-spherical but still zonally symmetric (so at a certain latitude; \phi is still not coupled)
* Dynamical consistency is defined as "the formal respect of converservation principles for axial angular momentum, energy and potential vorticity"
* This paper explores the outline created by White&Wood(2012,Ch6) (aka WW12)
* Geopotential is the gravitational potential of Earth's gravit field
* Orthogonal curvilinear coordinates \xi_1, \xi_2, \xi_3 (zonal, meridional and vertical directions)
  - All metric factors are independent of \xi_1 due to zonal symmetry
  - For gradient/curl/divergence of OCC, see WW12
  - Infinitesimal distance ds²=h_1²dxi_1² + h_2²dxi_2² + h_3²dxi_3²
    - Here the metric (scale) factors h_i are related to the cartesian coordinates x/y/z by the following identity:
    - h_i² \equiv (\frac{\deltax}{\delta\xi_i})² + (\frac{\deltay}{\delta\xi_i})² + (\frac{\deltaz}{\delta\xi_i})², i=1,2,3
* Material derivative describes the time rate of change of some physical quantity (velocity components in the OCC system in this case) of a material element subjected to a space-and-time dependent macroscopic velocity field variation of this quantity. ?So it's just the full derivative expressed as the sum of the partial derivatives (of the separate components)?
* The definition of apparent gravity g  in terms of the geopotential \Phi has been used: g \equiv \frac{1}{h_3}  \frac{d\Phi}{d\xi_3}



### r-Modes on Rapidly Rotating, Relativistic Stars. Do Type I Bursts excite modes in the Neutron Star Ocean, Heyl 2004
* q \equiv \nu  ; do note that Townsend2003 makes an approximation for \Omega to be much less than ~14000 (back-of-the-envelope estimation for (GM/R³)^½) and that Heyl states \Omega to be several hundred Hertz -- is "several hundred" indeed much lower?
* **HEYL states that modes should travel westward** IE that means m > 0, *but Townsend2003 has been using m=-2!* How much of this do I have to keep in mind? Heyl also states that m=-1 or 1; but that point has been shown to be mistaken, no?
* *Unstable burning during type I bursts produces mainly iron-group elements, so the ocean is much more shallow than in the constant rate Z sources.* Does it become shallower during the burst, or is it always more shallow?


---

# Books

### Black Holes, White Dwarfs, and Neutron stars, Shapiro & Teukolsky 1983

Chapter 2

* Global elements (large-scale) versus Local elements (small scale)
    - Global: gravity, electromagnetic fields, rotation etc
    - Local: pressure, viscosity, emissivity etc
* At high densities, inverse \beta-decay is the most important correction to the EoS
    - e + p -> n + \nu
    - Will assume that the neutrino's from this reaction escape the system
    - Reaction can proceed when e has enough energy (1.29MeV, mass diff between n and p, *c²)
* For densities above ~ 4e11 g/cm³ the n/p ratio becomes critical - any further increase in density will lead to *neutron drip*, which is a two-phase system where electrons, nuclei and **free neutrons** co-exist
    - The higher the density goes, the more free neutrons you get
    - Above 4e12 g/cm³, the neutrons add more pressure than the electrons. This medium, controlled by the neutron gas can be described as one large nucleus with a lower-than-normal nuclear density


Chapter 6

* Fluids recap, ?although it doesn't mention perturbations are only considered to first order?
* Stability criterium: E_2 = \delta²E = T_2 + V_2, where the sub_2 denotes variation of the second level, as the first level E_1 for the equilibrium energy is zero
    - T = kinetic energy of perturbation - can never be negative, per definition
    - V = potential energy of perturbation
    - If E_2 is **positive** for all initial data (\xi^i, d_t\xi^i) then V_2 will be positive and *thus the system will be stable*. On the other hand, if E_2 is **negative** for any (\xi^i, d_t\xi^i) then V_2 must be negative and there exists an instability
* Equivalent stability criteria are:
    - V_2 >= 0 for all perturbations
    - E_2 >= 0 for all perturbations
    - \omega² >= 0 for all modes
    - \bar\Gamma_1 >= 4/3 (radial stability only - its the pressure-averaged adiabatic index). \Gamma_1 = (\delta ln P) / (\delta ln \rho)
* General relativity tends to destabilize configurations, as gravity is stronger and thus collapse/instability comes easier
     - **Remember**; c = G = 1 for GR stuff
* GR can be used to rule out WD as pulsar candidates, since they cannot get below ~2s pulsation times and ms pulsars are known (p.161)
    - ?But why does it rule out slower pulsars, couldn't there be low mass low frequency pulsars that are actually WD? -- Geometry arguments that the slow pulsars are not that different from the fast ones so they're most likely also NS


Chapter 7

* 7.1 recaps the addition of magnetic fields into the fluid equations, useful background
* Difference between *secular* and *dynamic* instabilities in Maclaurin spheroids comes from dissipative terms - if a dissipative term is needed to cause the instability, it is called a *secular* instability. Otherwise it is a *dynamic* instability.
    - ?Still stable up to high eccentricities, so those instabilities should not impact me?
    - Dynamic instabilities grow on the dynamical timescale ~(G\rho)^-½
* Maclaurin spheroids beyond the bifurcation point (e>.81267) are secularly unstable to becoming **Jacobi** ellipsoids (*spinning rugbyball*) and **Dedekind** ellipsoids (*stationary rugbyball*, stationary shape but the ellipsoidal surface is maintained through the rotation of an inner fluid)
    - ?Jacobi ellipsoids are tri-axial, while Maclaurin spheres are bi-axial? -- You can rotate a Maclaurin sphere (no radial dependance on the shape of the sphere, Jacobi as a rugbyball does have this)
    - ?Do NS rotate uniformly? End of Ch7.3 - page 180 says realistic stars rotate **differentially**, at least in their outer layers
* Rotational energy has a steeper dependence on the adius than the internal energy in the relativistic limit
    - Equilibrium can always be achieved for *any* mass by decreasing the radius of the current configuration, so an equilibrium model can be constructed for *any* mass provided the angular momentum is nonzero. However, you might create a model which is so dense that it violates your EoS, so it is not necessarily a *physical* model
* Stellar contraction without angular momentum loss requires that T/|W| (T = rotational kinetic energy, W = gravitational potential energy) increases as 1/R, so rotation is likely more important in a CO than the MS progenitor
* Rotation tends to **stabilize** radial modes


Chapter 9

* Low-density NS with an ideal neutron gas EoS have the n=3/2 polytrope
    - R = 14.64 (\rho_c / 1e15 g/cm³)^(-1/6) km
    - M = 1.102 (\rho_c / 1e15 g/cm³)^.5 M_sol, so M = (15.12km / R)³ M_sol
    - In this calculation there is no minimum NS mass (\rho_c can go to zero), although at low density the NS will become unstable to \beta-decay
    - See page 245-247 for an approximate derivation, although it comes out ~40% too high (at 1.03 M_sol)
* Stiff EoS leads to a greater M_max than soft ones
* Stiff EoS leads to a lower \rho_c, higher R and thicker crust when compared to soft EoS *at the same mass*
* Different regions in NS can be identified (See Pandharipande, Pines and Smith 1976):
    - **Surface** (\rho <= 1e6 g/cm³), region where the temperatures and magnetic fields expected for most NS can significantly affect the EoS
    - **Outer Crust** (1e6 <= \rho <= 4.3e11 g/cm³), a solid region with a Coulomb lattice of heavu nuclei, which coexist in \beta-equilibrium with a relativistic degenerate electron gas
    - **Inner Crust** (4.3e11 <= \rho <= 2-2.4e14 g/cm³), a lattice of neutron-rich nuclei together with a superfuild neutron gas and an electron gas
    - **Neutron Liquid** (2-2.4e14 g/cm³), chiefly made up from superfluid neutrons with smaller concentrations of sluiderfluid protons and normal electrons
    - **Core** (\rho > \rho_core), which is unsure to exist in all stars, which might also depend on whether or not pion condensation occurs, or whether there is a transition to a neutron solid or quark matter or some other phase physicall distinct from a neutron liquid at densities above some critical value \rho_core
* Rapidly rotating configurations in general relativity are technically difficult to construct, with no simple stability criteria known. Existing calculations are build on assumptions:
    - Slow rotation (Hartle 1967, Hartle and Thorne 1968, Abramowicz and Wagoner 1976)
    - Uniform rotation and homogeneous configurations (Butterworth and Ipser 1975, 1976)
    - post-Newtonian gravity and an ideal Fermi gas EoS (Shapiro and Lightman 1976(b))
* ?If crust replacement takes place, what happens to the former crust - it moves down into the neutron liquid? So whatever is the makeup of the central regions of a NS, it can be created through *regular* means and does not depend on explosive creation techniques?



### Geophysical Fluid Dynamics (2nd edition), Pedlosky 1987

Chapter 3

* Dynamics of a shallow, rotating layer of a homogeneous incompressible and inviscid fluid
* Fundamental parametric condition for shallow-water theory: \delta = D/L << 1
    - D is the average depth of the layer
    - L is the characteristic horizontal length scale for the motion
* Because of incompressibility and constant density the dynamics and thermodynamics are decoupled
    - Mass conservation reduces to incompressibility condition deltau/deltax + deltav/deltay  +deltaw/deltaz = 0 (u, v, w are velocity components in the x, y, z direction respectively)
    - Take U the characteristic scale for horizontal velocity and W the scale for vertical velocity. The first two terms of the eq above goes as O(U/L) and thus it follows that W/D cannot be larger than this O(U/L), so W =< O(\delta U)
* Estimating the terms in the momentum equation (\rho[d**u**/dt + 2 **\Omega** \cross **u**] = -\nabla p + \rho \nabla \Phi + *F*) leads to the hydrostatic approximation, deltap/deltaz = -\rho g + O(\delta²)
* Integrating this new condition and applying the correct boundary condition leads to the conclusion that the horizontal pressure gradient is independent of z
    - So deltap/deltax = \rho g deltah/deltax
    - And deltap/deltay = \rho g deltah/deltay
    - So horizontal accelerations are independent of z and it is consistent to assume they will remain so at later times
* Let  the thickness of a layer H be defined as H(x, y, t) = H_0(x, y) + \eta(x, y, t) with H_0 >> \eta. Furthermore, suppose that u and v (x- and y-velocity) are small enough so that \delta**u_H**/\delta**t** is also much larger than **u_H** * \grad**u_H**
    - This allows you to reconstruct the linear forms of momentum and mass conservation (see page68, eq 3.6.3)
    - Now define the linearized mass flux vector **U** = **i**U + **j**V, with U = uH_0, V = vH_0
    - Further manipulation of this leads to an ODE for the velocities of u and v in terms of \eta, the perturbation of the initial height - see 3.6.12
* The time-independent forms of 3.6.12 imply that >(where f is the coriolis parameter)<
    - u = -g/f \delta\eta/\deltay
    - v = g/f \delta\eta/\deltax
    - These can be recognized as the geostrophic relation for the horizontal motions, and in particular the isolines of eta are streamlines for a steady geostrophic flow, as u\delta\eta/\deltax + v\delta\eta/\deltay = 0
    - Lines of constant undisturbed depth H_0, coincide with lines of constant \eta in the x,y plane. As isolines of \eta are streamlines of a steady geostrophic flow, this means that the linearized geostropic flow must be along lines of constant depth
    - Technically geostropic motion is only possibe if the contour lines of H_0 close on themselves or extend to infinity, however real motions are not precisely geostropic, but have relaxed steadiness or linearity constraints
* For a solution of the form \eta = Re(\eta_0 e^(i(kx + ly - \simgat))), one can establish a dispertion relation:
    - \sigma(**K**) = \pm{f²+C_0²K²}^½, where **K** is the wave vector and K is the wave number, with K=|**K**|, and where C_0² = gH_0
    - This also means two free oscillations are present, which represent waves with phase speeds C = \pm{C_0² + f²/k²}^½
    - For no rotation (so f=0) the phase at all wavelengths has the same speed; the shallow-water speed of classical linear theory. If there is rotation, the wave speed is increased
* The Poincaré waves discussed in 3.9 (possibility (i) on page 76) is called g-modes in eg the Townsend paper, ?check that this is indeed the same?
    - They arise when \alpha² = n²\pi²/L² = (\simga² - f²)/C_0² - k² for n = int =/= 0
    - The link in \alpha² equations leads to: \simga_n = \pm {f² + C_0²(k² + n²\pi²/L²)}^½ for n=1,2,3,... Do note the similarity to the dispertion relation above, except that the y-component of the wave vector is now quantized as an integral multiple of \pi/L. Also note that n = 0 is not a valid solution because the wave field would then have no variations in the y-axis, but there are now y-boundaries and thus for a rotating fluid this cannot be done
    - Poincaré waves propagate their phase equally well in both positive and negative x-direction, and the frequency always exceeds f because the cross-stream wave number is quantized: \simga >= {f² + C_O²\pi²/L²}^½
    - Equations 3.9.16 describe the dynamical fields for each mode
* Possibility (ii) is a Kelvin wave, which illustrates that the simple balance-of-terms considerations need to be refined when the horizontal scales of the motion are not isotropic
* The third possibility (\simga = f) is a spurious (fake) root of this eigenvalue problem, as the only working solution is a wave indistinguishable from the Kelvin wave
* ?Doesn't equation 3.11.3 have the terms in the d/dt[] brackets the wrong way around, coming from 3.6.9?
* Note for paper-writing; 3.12 has a helpful introduction as to why we're actually making the assumptions and where they come from & what we typically do to solve problems through the approximations 
    - It also (eventually) introduces asymptotic series
* ?Latitude distance Y (p106) is the surface distance from the equator?
* ?How much of Ch3.17 applies to a rapidly rotating sphere, as in do some/all assumptions hold in a very oblate case?
* Rossby waves in a Zonal Current, do be careful with "eastern/western" flows, as they refer to the direction *the wave is travelling*, which is different from the meteorological naming, where those terms refer to the *origin of the flow* (eg in fluid lingo an eastern stream is **headed** east, while in meteorology an eastern stream **comes** from the east)
    - **I will follow the fluid lingo**
* Stationary (Rossby) flows are only possible in the western flow, if K=K_s=\beta^½ - ?This isn't just for a stationary sphere anymore, right - since f_0 and \beta_0 (3.17.6) depend on \Omega?
    - ?Since Earth is rotating eastward, this means only contra-moving waves can be stationary (which makes sense i guess)?
    - ?In Townsend 2003, m\nu > 0 is a retrograde direction, so both \lambda+ and - have retrograde directions, but only the \lambda- are Rossby waves? Is is because the + solution ends at \lamda+ = m², while we are under the assumption that \lambda =/= m² ergo the solution should be ruled out => only the retrograde Rossby wave (\lambda-) remains as a solution in the 0<m\nu<2m² region?




---
# General Notes/comments

* Accreted crust is also called a dirty crust (by Brown)



