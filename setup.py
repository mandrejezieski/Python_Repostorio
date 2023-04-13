import sys
from cx_Freeze import setup, Executable
import pygame


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("script.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [pygame, sys, locals(),random],
        include_files = [],
        excludes = []
)

setup(
    name = "Test_cobrinha_002.py",
    version = "1.0",
    description = ": GAME DA COBRINHA : ",
    options = dict(build_exe = buildOptions),
    executables = executables
 )