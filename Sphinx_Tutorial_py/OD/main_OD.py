
"""
OrbitalElementsFromCartState.py
================================
Compute orbital elements from cartesian state vectors.
"""


import math

def OrbitEnergyFromCartState(rMag, vMag, Gm):
    """ Summary Line....

        Extended description of function.

    
        Parameters
        ----------
        rMag:   (m)
             scalar position magnitude 
        vMag:   (m/s)  
            scalar velocity magnitude
        Gm:     (m^3/sec^2)    
            gravitational param 


        Yields
        -------
        Orbit Energy:   (m^2/s^2)
            orbit energy from Cartesian state 


        Raises
        ------
        ZeroDivisionError
            if ``rMag`` is equal to 0

    """

    if rMag == 0:
        raise ZeroDivisionError('Can not divide by zero')

    return (vMag**2 / 2) - Gm / rMag


def SemimajorAxisFromCartState(rMag, vMag, Gm):
    """ Summary Line....

        Extended description of function.

        Parameters
        ----------
        rMag:   (m)
             scalar position magnitude 
        vMag:   (m/s)  
            scalar velocity magnitude
        Gm:     (m^3/sec^2)    
            gravitational param 


        Yields
        -------
        Semimajor Axis: (m)
            semimajor axis from Cartesian state 


        Raises
        ------
        ZeroDivisionError
            if ``orbitEnergy`` is equal to zero

    """

    orbitEnergy = OrbitEnergyFromCartState(rMag, vMag, Gm)

    if orbitEnergy == 0:
        raise ZeroDivisionError('Can not divide by zero')

    SemimajorAxisFromCartState = -Gm / (2 * orbitEnergy)

    return SemimajorAxisFromCartState

def OrbitPeriodFromSma(sma, Gm):
    """ Summary Line....

        Extended description of function.

        Parameters
        ----------
        sma:    (m)
            semimajor axis 
        Gm:     (m^3/sec^2)
            gravitational param 


        Yields
        -------
        Orbit Period:   (s)
            orbit period from semimajor axis 


        Raises
        ------
        ZeroDivisionError
            if ``Gm`` is equal to zero

        ValueError
            if ``Gm`` or ``sma`` are negative

        ValueError
            if ``OrbitPeriodFromSma`` is negative or zero

    """
 

    if Gm == 0:
        raise ZeroDivisionError('Can not divide by zero')

    if Gm < 0 or sma < 0:
        raise ValueError('Can not take a square root of a negative number')

    OrbitPeriodFromSma = 2 * math.pi * math.sqrt(sma**3 / Gm)

    if OrbitPeriodFromSma <= 0:
        raise ValueError('Orbit Period should not be negative or zero')

    return OrbitPeriodFromSma