"""
mdi_mechanic.py
A tool for testing and developing MDI-enabled projects.

Handles the primary functions
"""

import os
import shutil
from . import cmd_report
from . import cmd_build
from . import cmd_run
from . import cmd_rundriver
from . import cmd_interactive
from .utils import utils as ut

def command_report():
    print("Starting a report")
    report_dir = os.getcwd()
    cmd_report.generate_report( report_dir )

def command_build( args ):
    print("Starting the installation")

    build_type = args.pop("build_type")

    if ( build_type != "dev" and build_type != "release"):
        raise Exception("Error: invalid argument to --type option.")

    report_dir = os.getcwd()
    cmd_build.install_all( report_dir, build_type )

def command_startproject( args ):
    print("Starting a new MDI project")
    project_type = args.pop("projecttype")

    base_path = os.getcwd()
    package_path = ut.get_package_path()

    if project_type == "enginereport":
        project_path = os.path.join( package_path, "mdimechanic", "projects", "enginereport" )

        print("Starting an engine report project")

        yml_path = os.path.join( base_path, "mdimechanic.yml" )
        docker_path = os.path.join( base_path, "docker" )
        gitignore_path = os.path.join( base_path, ".gitignore" )
        if os.path.exists( yml_path ) or os.path.exists( docker_path ):
            raise Exception("This already appears to be an MDI project")

        yml_source = os.path.join( project_path, "mdimechanic.yml" )
        docker_source = os.path.join( project_path, "docker" )
        workflow_source = os.path.join( project_path, ".github" )
        gitignore_source = os.path.join( project_path, ".gitignore" )
        shutil.copyfile( yml_source, yml_path )
        shutil.copytree( docker_source, docker_path )
        shutil.copyfile( gitignore_source, gitignore_path )

    else:
        raise Exception("Unrecognized project type.")

def command_run( args ):
    run_dir = os.getcwd()
    print("Running a custom calculation with MDI Mechanic.")
    script_name = args.pop("script_name")
    debug = args.pop("debug", False)  


    if script_name is None:
        raise Exception("Error: --name argument was not provided.")

    # Test the driver
    try:
        cmd_run.run( script_name, run_dir, debug=debug )
        print("Success: The driver ran to completion.")
    except:
        raise Exception("Error: The script did not complete successfully.")

def command_rundriver( args ):
    report_dir = os.getcwd()
    print("Running an MDI test driver.")
    driver_name = args.pop("driver_name")

    # Test the driver
    try:
        cmd_rundriver.test_driver( driver_name, report_dir )
        print("Success: The driver ran to completion.")
    except:
        raise Exception("Error: The test driver did not complete successfully.")

def command_interactive( args ):
    run_dir = os.getcwd()
    image_name = args.pop("image_name")

    try:
        cmd_interactive.start( image_name, run_dir )
        print("Success: Interactive session completed successfully.")
    except:
        raise Exception("Error: Interactive session did not complete successfully.")
