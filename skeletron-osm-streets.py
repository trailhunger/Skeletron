from sys import argv, stdin, stderr, stdout
from itertools import combinations
from optparse import OptionParser
from csv import DictReader
from re import compile
from json import dump
from math import pi

from Skeletron import waynode_networks, networks_multilines
from Skeletron.input import parse_street_waynodes
from Skeletron.output import multilines_geojson
from Skeletron.util import open_file

earth_radius = 6378137

optparser = OptionParser(usage="""%prog <osm input file> <geojson output file>""")

defaults = dict(zoom=12, width=10, use_highway=True)

optparser.set_defaults(**defaults)

optparser.add_option('-z', '--zoom', dest='zoom',
                     type='int', help='Zoom level. Default value is %s.' % repr(defaults['zoom']))

optparser.add_option('-w', '--width', dest='width',
                     type='float', help='Line width at zoom level. Default value is %s.' % repr(defaults['width']))

optparser.add_option('--ignore-highway', dest='use_highway',
                     action='store_false', help='Ignore differences between highway tags (e.g. collapse primary and secondary) when they share a name.')

if __name__ == '__main__':
    
    options, (input_file, output_file) = optparser.parse_args()
    
    buffer = options.width / 2
    buffer *= (2 * pi * earth_radius) / (2**(options.zoom + 8))
    
    #
    # Input
    #
    
    input = open_file(input_file, 'r')
    
    ways, nodes = parse_street_waynodes(input, options.use_highway)
    networks = waynode_networks(ways, nodes)
    multilines = networks_multilines(networks)
    
    #
    # Output
    #
    
    kwargs = dict(buffer=buffer, density=buffer/2, min_length=2*buffer, min_area=(buffer**2)/4)
    
    if options.use_highway:
        key_properties = lambda (name, highway): dict(name=name, highway=highway)
    else:
        key_properties = lambda (name, ): dict(name=name)

    print >> stderr, 'Buffer: %(buffer).1f, density: %(density).1f, minimum length: %(min_length).1f, minimum area: %(min_area).1f.' % kwargs
    print >> stderr, '-' * 20

    geojson = multilines_geojson(multilines, key_properties, **kwargs)
    output = open_file(output_file, 'w')
    dump(geojson, output)