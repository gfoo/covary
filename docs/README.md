## Prepare Python env (first time)

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Generate doc

```
source ./venv/bin/activate
make html
```

Open in browser build/html/index.html

The doc pushed on main branch is automaticqlly pushed to [GitHub Pages of the project](https://gfoo.github.io/covary/index.html)