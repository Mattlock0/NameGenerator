# NameGenerator
Mattlock's name generator! With this project, you can generate any names you wish from templates and change the settings while you're at it.

If you're running from cli.py, make sure the CONFIG_PATH (main.py, line 13) is set to RUN_CONFIG_PATH.

To build, run:

    pyinstaller cli.py --name namegenerator --onefile -w

Or leave out the `-w` for debug.

If it's having trouble finding the config file, add the following lines to namegenerator.spec:

    import shutil
    
    shutil.copyfile('data/settings.ini', '{0}/settings.ini'.format(DISTPATH))

And rerun with:

    pyinstaller --clean namegenerator.spec