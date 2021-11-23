# coding=utf-8
'''
    为python脚本指定运行参数，提供传参help
    采集传参
'''
import optparse
import sys

option = optparse.OptionParser()
option.add_option('-s', '--start-directory', dest='start', default='.',
                          help="Directory to start discovery ('.' default)")
option.add_option('-p', '--pattern', dest='pattern', default='test*.py',
                          help="Pattern to match tests ('test*.py' default)")
option.add_option('-t', '--top-level-directory', dest='top', default=None,
                          help='Top level directory of project (defaults to start directory)')

argvs = sys.argv

values,argv = option.parse_args(argvs)

start = values.start
pattern = values.pattern
top = values.top

print "start:",start
print "pattern:",pattern
print "top:" ,top


