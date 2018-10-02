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
    - ?How much prove do I need to show that they are solutions / *how* do I show it, or can I skip that in my thesis (and just say "as noted by e.g. Townsend 2003, they are solutions")?


* !Math questions below!
* ~~?Eq 17 in the paper has minus signs on the LHS; I do not have any minus signs in my version of eq17, but I do get the matching Y_\perp:Y_p equation (14)? -- ??Checked with Frank he also doesn't get the - signs, and when checking with Bildsten 1996 paper to recover L_\mu=-\lambda (eq6 for L_\mu) it looks like I need the - signs to get it to work??~~
    - ~~?Eq 18 **is** correct when following Townsend2003, and I can recover the L_\mu=-\lambda equation (plus an extra term? but still got the other 3 correctly...) so what are we missing on the eq17 minus signs?~~
    - **SOLVED**; the issue was that a minus sign was missing in the middle term of eq20, which would flip the sign on eq17 correctly (and does indeed result in the correct signs for eq19 which otherwise also would've had that issue, but is now correct)
* ?Can reproduce eq15/19 without the lambda too - why does it come in **here** and not somewhere else? Specifically because this is the continuity equation? -- Technically supposed to put it in for 14/17 and 14/18 too, but try and put in "\alpha" and add "\beta" instead of \lambda and the functions of \alpha and \beta are coupled so that you can set \alpha/alpha = 1 and \beta/\alpha = \lambda and thus only have one parameter



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



---
# General Notes/comments

* Accreted crust is also called a dirty crust (by Brown)



