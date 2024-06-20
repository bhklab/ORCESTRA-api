from pathlib import Path

import aiohttp
from git import GitCommandError, Repo

async def validate_github_repo(url: str) -> bool:
    """This function validates a GitHub repository.

    Args:
      url (str): The URL of the GitHub repository to validate.

    Returns:
      bool: True if the repository is valid (status code 200), False otherwise.

    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return True
            return False


async def clone_github_repo(url: str, dest: Path) -> Repo:
    """Clone a GitHub repository.

    Args:
      url (str): The URL of the GitHub repository to clone.
      dest (Path): The destination path where the repository will be cloned.

    Returns:
      Repo: The cloned repository object.

    Raises:
      Exception: If the destination directory already exists.
      GitCommandError: If there is an error while cloning the repository.
      Exception: If there is an unexpected error during the cloning process.
    """
    # check if dest exists
    if not dest.exists():
        dest.mkdir(parents=True)
    else:
        raise Exception(f'Directory: {dest} already exists.')

    try:
        return Repo.clone_from(url, dest)
    except GitCommandError as git_error:
        raise git_error
    except Exception as e:
        raise e


async def pull_github_repo(repo: Repo) -> Repo:
    """Pull changes from a GitHub repository.

    Args:
      repo (Repo): The repository object to pull changes from.

    Returns:
      Repo: The repository object with the pulled changes.

    Raises:
      GitCommandError: If there is an error while pulling the changes.
    """
    try:
        repo.remotes.origin.pull()
        return repo
    except GitCommandError as git_error:
        raise git_error


async def pull_latest_pipeline(dest: Path) -> Repo:
    """Pull the latest changes from a GitHub repository.

    Args:
      dest (Path): The destination path where the repository is cloned.

    Returns:
      Repo: The repository object with the pulled changes.

    Raises:
      GitCommandError: If there is an error while pulling the changes.
    """
    try:
        repo = Repo(dest)
        return await pull_github_repo(repo)
    except GitCommandError as git_error:
        raise git_error
