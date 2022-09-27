# ACTS full chain

## Build ACTS

```
git clone https://github.com/acts-project/acts.git

cd acts

git submodule update --init

mkdir build

cmake -S . -B build -GNinja \
  -DACTS_BUILD_PLUGIN_DD4HEP=ON \
  -DACTS_BUILD_EXAMPLES=ON \
  -DACTS_BUILD_EXAMPLES_PYTHON_BINDINGS=ON \
  -DACTS_BUILD_EXAMPLES_DD4HEP=ON \
  -DACTS_BUILD_ODD=ON
```

Alternative setup [here](https://codimd.web.cern.ch/A108z_6tRiWJaIa5yAabdg).
