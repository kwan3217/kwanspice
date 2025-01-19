import pytest

from kwanspice.mkspk import mkspk


def test_mkspk():
    """
    Follow the example in the MKSPK user guide
    :return: None, but raises an exception if the test fails
    """
    mkspk(oufn='data/test_mkspk_505.bsp',
          fmt=['s','.3f','.3f','.3f','.6f','.6f','.6f'],
          data=[['1979 MAR 05 00:00:00',-178932.619,-28063.045,-17448.755,4.733702,-23.495860,-11.041956],
                ['1979 MAR 05 00:02:00',-178337.419,-30878.143,-18771.071,5.186043,-23.421245,-10.996084],
                ['1979 MAR 05 00:04:00',-177688.033,-33683.859,-20087.682,5.636786,-23.339517,-10.946873]],
          input_data_type='STATES',
          output_spk_type=5,
          object_id=505,
          object_name='AMALTHEA',
          center_id  = 599,
   center_name       = 'JUPITER',
   ref_frame_name    = 'B1950',
   producer_id       = 'N.G.Khavenson, IKI RAS, Russia',
   data_order        = 'EPOCH X Y Z VX VY VZ',
   input_data_units  = ('ANGLES=DEGREES', 'DISTANCES=km'),
   data_delimiter    = ' ',
   leapseconds_file  = 'data/naif0012.tls',
   pck_file          = 'data/Gravity.tpc',
   segment_id        = 'SPK_STATES_05',
          comment="""
          This is a multiline comment
          that goes at the beginning of the generated kernel.
          Also, my hovercraft is full of eels."""
          )