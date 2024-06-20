"""This module contains functions for executing commands in a shell."""

import asyncio
import subprocess
from typing import List, Tuple, Union

from orcestrator.common.logging.logging_config import get_logger

logger = get_logger()


async def execute_command(command: Union[str, List[str]]) -> Tuple[str, str]:
    """This function executes a command in a shell asynchronously.

    It captures both the standard output and the standard error of the command
    and returns them
    """

    if isinstance(command, str):
        command = command.split()

    logger.debug(f"Executing command: {' '.join(command)}")
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
    logger.info(f'stdout:\n{stdout}')


if __name__ == '__main__':
    asyncio.run(main())
