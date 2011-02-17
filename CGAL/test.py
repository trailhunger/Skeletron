import _skeletron
import pprint
polygon = [
  [
    [29.355902, 71.448935],
    [28.786797, 71.213203],
    [20.000000, 50.000000],
    [28.786797, 28.786797],
    [50.000000, 20.000000],
    [200.000000, 20.000000],
    [221.213203, 28.786797],
    [271.213203, 78.786797],
    [280.000000, 100.000000],
    [280.000000, 250.000000],
    [271.213203, 271.213203],
    [250.000000, 280.000000],
    [50.000000, 280.000000],
    [28.236465, 270.648209],
    [20.041465, 248.423235],
    [29.355902, 71.448935]
  ],
  [
    [88.988891, 80.000000],
    [81.620470, 220.000000],
    [220.000000, 220.000000],
    [220.000000, 112.426407],
    [187.573593, 80.000000],
    [88.988891, 80.000000]
  ]
]
edges = _skeletron.skeleton(polygon)
pprint.pprint( edges )