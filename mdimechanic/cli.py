"""
Provides a CLI for MDI_Mechanic
"""

import argparse
import subprocess
import sys
from . import commands

from .utils import utils as ut

def parse_args():
    parser = argparse.ArgumentParser(description="A CLI for the MDI_Mechanic.")

    subparsers = parser.add_subparsers(dest="command")

    build = subparsers.add_parser("build", help="Build containers for MDI_Mechanic and the engine.")
    #build.add_argument("location", type=str, help="The location where the engine is located.")
    build.add_argument("--type", dest='build_type',
                     type=str,
                     default="dev",
                     help="Type of build. (\"dev\" [Default] or \"release\")")

    startproject = subparsers.add_parser("startproject", help="Start a new MDI project.")
    startproject.add_argument("--enginereport", dest='projecttype', action='store_const',
                              const="enginereport", default=None,
                              help="Start an engine report project.")

    report = subparsers.add_parser("report", help="Create a report for the engine.")

    run = subparsers.add_parser("run", help="Run a code.")
    run.add_argument("--name", dest='script_name',
                     type=str,
                     default=None,
                     help="Name of the script to run.")
    
    run.add_argument("--debug", action='store_true', help="Enable debug mode for real-time output")  


    rundriver = subparsers.add_parser("rundriver", help="Run a calculation with a test driver.")
    rundriver.add_argument("--name", dest='driver_name',
                           type=str,
                           default=None,
                           help="Name of the test driver to run.")

    interactive = subparsers.add_parser("interactive", help="Start an interactive session within a container.")
    interactive.add_argument("--image", dest='image_name',
                             type=str,
                             default=None,
                             help="Name of the image to run interactively.")

    args = vars(parser.parse_args())
    if args["command"] is None:
        parser.print_help(sys.stderr)
        exit(1)

    return args

def main(args=None):
    
    if args is None:
        args = parse_args()

    command = args.pop("command")
    if command == "build":
        commands.command_build( args )
    elif command == "report":
        commands.command_report()
    elif command == "startproject":
        commands.command_startproject( args )
    elif command == "run":
        commands.command_run( args )
    elif command == "rundriver":
        commands.command_rundriver( args )
    elif command == "interactive":
        commands.command_interactive( args )
