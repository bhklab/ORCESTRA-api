"""This module contains functions for executing commands in a shell."""

import asyncio
import subprocess
from typing import List, Tuple, Union

async def execute_command(command: Union[str, List[str]]) -> Tuple[str, str]:
    """This function executes a command in a shell asynchronously.

    It captures both the standard output and the standard error of the command
    and returns them
    """

    if isinstance(command, str):
        command = command.split()

    process = await asyncio.create_subprocess_exec(
        *command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    return stdout, stderr


async def main() -> None:
    """Main function for testing the module."""
    stdout, stderror = await execute_command('snakemake --version')
