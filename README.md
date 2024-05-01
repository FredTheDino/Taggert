# Taggert
A quick PureScript-tags generator cobbled together to be able to work

# Usage
```
./taggert some/**/purs/files/*.purs > tags
./taggert > tags # (Defaults to .spago/**/*.purs and lib/**/*.purs)
# Or in a script
find -type f -name "*.purs" | taggert > tags
```
