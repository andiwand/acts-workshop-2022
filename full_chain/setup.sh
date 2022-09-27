. ~/cern/install/root/bin/thisroot.sh
. ~/cern/install/DD4hep/bin/thisdd4hep.sh
. ~/cern/install/acts/bin/this_acts.sh

# python deps
. ~/cern/venv/bin/activate

# acts python
. ~/cern/install/acts/python/setup.sh
export PYTHONPATH="${PYTHONPATH}":~/cern/source/acts/Examples/Scripts/Python

# root include path
export ROOT_INCLUDE_PATH="${ROOT_INCLUDE_PATH}":~/cern/install/podio/include
export ROOT_INCLUDE_PATH="${ROOT_INCLUDE_PATH}":~/cern/install/EDM4hep/include

# cmake
export CMAKE_PREFIX_PATH=~/cern/install/root:~/cern/install/Geant4:~/cern/install/DD4hep:~/cern/install/acts:~/cern/install/LCIO:~/cern/install/podio:~/cern/install/EDM4hep:~/cern/install/pythia8

