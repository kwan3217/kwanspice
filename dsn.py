"""
Conversion of DSN station coordinates to latitude and longitude

References:

    [1] "301 Coverage and Geometry." DSN No. 810-005, 301, Rev. M
          Issue Date: September 04, 2020. JPL D-19379; CL#20-3996.

          URL: https://deepspace.jpl.nasa.gov/dsndocs/810-005/301/301M.pdf
    [2] "SPK for DSN Station Locations" comment file
          URL: https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/stations/earthstns_fx_201023.cmt

"""

dss_xyz={
    # Coordinates copied from [2] and reformatted. [2] itself uses [1] as a reference.
    #Station locations in the ITRF93 frame at the specified epoch are:
    #       Antenna  Diameter   x (m)            y (m)           z (m)
    #Goldstone
              13:      (34, -2351112.659    -4655530.636    +3660912.728),
              14:      (70, -2353621.420    -4641341.472    +3677052.318),
              15:      (34, -2353538.958    -4641649.429    +3676669.984), # {3}
              24:      (34, -2354906.711    -4646840.095    +3669242.325),
              25:      (34, -2355022.014    -4646953.204    +3669040.567),
              26:      (34, -2354890.797    -4647166.328    +3668871.755),
    # Canberra
              34:      (34, -4461147.093    +2682439.239    -3674393.133), # {1}
              35:      (34, -4461273.090    +2682568.925    -3674152.093), # {1}
              36:      (34, -4461168.415    +2682814.657    -3674083.901), # {1}
              43:      (70, -4460894.917    +2682361.507    -3674748.152),
              45:      (34, -4460935.578    +2682765.661    -3674380.982), # {3}
    # Madrid
              53:      (34, +4849339.965     -360658.246    +4114747.290), # {2}
              54:      (34, +4849434.488     -360723.8999   +4114618.835),
              55:      (34, +4849525.256     -360606.0932   +4114495.084),
              56:      (34, +4849421.679     -360549.659    +4114646.987),
              63:      (70, +4849092.518     -360180.3480   +4115109.251),
              65:      (34, +4849339.634     -360427.6637   +4114750.733)

    #   Notes from [1]:
    #
    #   {1} Position absolute accuracy estimated to be +/- 3cm (0.030m)
    #       (1-sigma) for each coordinate.
    #
    #   {2} Position absolute accuracy estimated to be +/- 3m (3-sigma)
    #       for each coordinate.

    #   {3} Decommissioned. For historical reference only.
}

from kwanmath import xyz2lla
