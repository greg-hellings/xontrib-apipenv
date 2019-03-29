# xonsh-pipenv

Automatically activate a [`pipenv`](https://github.com/pypa/pipenv)
virtual environment when changing `pipenv` project directories.

- `pipenv shell` does not play nice with `xonsh` (see
[here](https://github.com/xonsh/xonsh/issues/2663) and
[here](https://github.com/pypa/pipenv/issues/498#issuecomment-417326930)
)

- This `xontrib` uses
[`vox`](https://github.com/xonsh/xonsh/blob/master/docs/python_virtual_environments.rst)
to activate the virtual environment created by `pipenv`

Installation / Usage
--------------------

1. Clone the repo and install

    ```
    git clone https://github.com/deeuu/xonsh-pipenv.git
    xpip install ./xonsh-pipenv
    ```

2. Add `xontrib load xonsh-pipenv` to your `.xonshrc`

3. To turn on auto activation with `$AUTO_PIPENV = True`

4. Now move to a `pipenv` project directory and watch `vox` automatically
   activate the virtual environment. Move to a second `pipenv` project and the
   virtual environment will switch

5. Use `vox deactivate` to deactivate

Note:
If you just want to activate a `pipenv` virtual environment, use the alias
`vox-activate-pipenv`.

Credits
---------

- [@rca](https://github.com/rca) for the [`vox`-based activation hack](https://github.com/xonsh/xonsh/issues/2663#issuecomment-394702058)

- This package was created with
[cookiecutter](https://github.com/audreyr/cookiecutter) and the
[xontrib](https://github.com/laerus/cookiecutter-xontrib) template.
