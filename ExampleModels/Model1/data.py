from SloppyCell.ReactionNetworks import *
expt = Experiment('expt1')
data = {'net1':{
  'x0': {
    0.0: (2.0, 0.1),
    0.1: (2.0, 0.1),
    0.2: (2.0, 0.1),
    0.30000000000000004: (2.0, 0.1),
    0.4000000000000001: (2.0, 0.1),
    0.5000000000000001: (2.0, 0.1),
    0.6000000000000001: (2.0, 0.1),
    0.7000000000000001: (2.0, 0.1),
    0.8: (2.0, 0.1),
    0.9: (2.0, 0.1),
  },
  'x1': {
    0.0: (5.0e-2, 0.1),
    0.1: (0.249281, 0.1),
    0.2: (0.448562, 0.1),
    0.30000000000000004: (0.647843, 0.1),
    0.4000000000000001: (0.847124, 0.1),
    0.5000000000000001: (1.04641, 0.1),
    0.6000000000000001: (1.24569, 0.1),
    0.7000000000000001: (1.44497, 0.1),
    0.8: (1.64425, 0.1),
    0.9: (1.84353, 0.1),
  },
  'x2': {
    0.0: (5.0e-2, 0.1),
    0.1: (4.97483e-2, 0.1),
    0.2: (4.94966e-2, 0.1),
    0.30000000000000004: (4.92449e-2, 0.1),
    0.4000000000000001: (4.89932e-2, 0.1),
    0.5000000000000001: (4.87415e-2, 0.1),
    0.6000000000000001: (4.84898e-2, 0.1),
    0.7000000000000001: (4.82381e-2, 0.1),
    0.8: (4.79864e-2, 0.1),
    0.9: (4.77347e-2, 0.1),
  },
  'x3': {
    0.0: (5.0e-2, 0.1),
    0.1: (4.94423e-2, 0.1),
    0.2: (4.88857e-2, 0.1),
    0.30000000000000004: (4.833e-2, 0.1),
    0.4000000000000001: (4.7775e-2, 0.1),
    0.5000000000000001: (4.72208e-2, 0.1),
    0.6000000000000001: (4.66671e-2, 0.1),
    0.7000000000000001: (4.61139e-2, 0.1),
    0.8: (4.5561e-2, 0.1),
    0.9: (4.50083e-2, 0.1),
  },
  'x4': {
    0.0: (5.0e-2, 0.1),
    0.1: (5.06831e-2, 0.1),
    0.2: (5.12942e-2, 0.1),
    0.30000000000000004: (5.18334e-2, 0.1),
    0.4000000000000001: (5.23008e-2, 0.1),
    0.5000000000000001: (5.26962e-2, 0.1),
    0.6000000000000001: (5.30198e-2, 0.1),
    0.7000000000000001: (5.32714e-2, 0.1),
    0.8: (5.34512e-2, 0.1),
    0.9: (5.3559e-2, 0.1),
  },
  'x5': {
    0.0: (0.0, 0.1),
    0.1: (-0.199975, 0.1),
    0.2: (-0.399974, 0.1),
    0.30000000000000004: (-0.599995, 0.1),
    0.4000000000000001: (-0.80004, 0.1),
    0.5000000000000001: (-1.00011, 0.1),
    0.6000000000000001: (-1.2002, 0.1),
    0.7000000000000001: (-1.40031, 0.1),
    0.8: (-1.60045, 0.1),
    0.9: (-1.80061, 0.1),
  },
  'x6': {
    0.0: (2.0, 0.1),
    0.1: (2.00023, 0.1),
    0.2: (2.00047, 0.1),
    0.30000000000000004: (2.0007, 0.1),
    0.4000000000000001: (2.00093, 0.1),
    0.5000000000000001: (2.00117, 0.1),
    0.6000000000000001: (2.0014, 0.1),
    0.7000000000000001: (2.00164, 0.1),
    0.8: (2.00187, 0.1),
    0.9: (2.0021, 0.1),
  },
  'x7': {
    0.0: (0.0, 0.1),
    0.1: (7.19e-4, 0.1),
    0.2: (1.438e-3, 0.1),
    0.30000000000000004: (2.157e-3, 0.1),
    0.4000000000000001: (2.876e-3, 0.1),
    0.5000000000000001: (3.595e-3, 0.1),
    0.6000000000000001: (4.314e-3, 0.1),
    0.7000000000000001: (5.033e-3, 0.1),
    0.8: (5.752e-3, 0.1),
    0.9: (6.471e-3, 0.1),
  },
}}