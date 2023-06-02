Conda is an environment manager for python. Miniconda is a lightweight 
version of Conda that is more barebones (as Conda was initially designed
for research and has a lot of bloat).

To install miniconda on Mac using Homebrew, use:
    brew install miniconda
    conda init zsh

To create a conda environment, run:
    conda create python={PYTHON VERSION (ex: '3.9')} -n {ENV_NAME}
    conda create python=3.9 -n cs35L

To activate an env, run:
    conda activate {ENV_NAME}
    conda activate cs35L


Once inside the environment, all packages installed using pip will only be
local to the environment (i.e. will not affect other environments, including
your computer's base/default one). Python packages can simply be run using
'python file_name' as the default Python version in the environment will
be the one you used to create it.

