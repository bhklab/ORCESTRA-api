# Git Requirements


1. Clone the Repository
   1. when a pipeline is registered, should clone the repository
   2. Errors:
      1. if the repository does not exist
      2. if the repository is private
      3. if the repository is not accessible
2. Pull the Repository
   1. initialized pipeline, whenever run-pipeline is called, should pull the repository for latest updates
   2. Bonus: return a message if the repository is up-to-date or a list of commits since the last pull
   3. Errors:
      1. if the repository does not exist (anymore)
      2. if the repository is now private
      3. if the repository is not accessible anymore
