# NameGenerator
Welcome to Mattlock's name generator! The purpose of this project is not to copy other name generators. NameGenerator creates unbiased, random names based on the structures of consonants and vowels found in the English language. They're rarely perfect names you can use straight from the generator, but they can provide a starting point from which to create totally original names! There are zero limitations on what can and cannot be generated, so be aware.

If you're running from cli.py, make sure the CONFIG_PATH (main.py, line 13) is set to RUN_CONFIG_PATH.

To build, run:

    pyinstaller cli.py --name namegenerator --onefile -w

Or leave out the `-w` for debug.

If it's having trouble finding the config file, add the following lines to namegenerator.spec:

    import shutil
    
    shutil.copyfile('data/settings.ini', '{0}/settings.ini'.format(DISTPATH))

And rerun with:

    pyinstaller --clean namegenerator.spec
