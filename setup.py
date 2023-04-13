import pygame
import sys
from cx_Freeze import setup, Executable



base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("script.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [pygame, sys, locals()],
        include_files = [],
        excludes = []
)

setup(
    name = "Test_002.py",
    version = "1.0",
    description = ".",
    options = dict(build_exe = buildOptions),
    executables = executables
 )