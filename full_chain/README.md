# ACTS full chain

```
cmake -S . -B build_key4hep -GNinja \
  -DACTS_BUILD_PLUGIN_DD4HEP=ON \
  -DACTS_BUILD_EXAMPLES=ON \
  -DACTS_BUILD_EXAMPLES_PYTHON_BINDINGS=ON \
  -DACTS_BUILD_EXAMPLES_DD4HEP=ON \
  -DACTS_BUILD_ODD=ON
```