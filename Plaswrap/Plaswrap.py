#!/usr/bin/env python

__author__ = "You CHE"
__license__ = "MIT"
__email__ = "youche@hku.hk"
__status__ = "Development"

import sys
import Plaswrap.argumentparser
import Plaswrap.manager

def main():
    if sys.version_info[0] < 3:
        print('''
        Please run Plaswrap with python3!!!⚠️ 
        ''')
        sys.exit(1)
        
    args = Plaswrap.argumentparser.parse_args(sys.argv[1:])
    Plaswrap.manager.Manager().main(args)

if __name__ == '__main__':
    main()
