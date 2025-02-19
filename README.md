# NameGenerator
Welcome to Mattlock's name generator! You will find that this generator is very different from others. It does not draw from a list of existing names, or uses AI to create similar-sounding ones, or anything of the sort.

NameGenerator creates unbiased, "random" names based on the structures of vowels and consonants found in the English language. It comes prepackaged with a few of these templates, plus the ability to make your own. To cut down on the randomness, NameGenerator also offers tunings which can narrow down the sort of name structure you're looking for (such as with common letter pairs, diagraphs, and double letters).

While using the default settings for tunings, the names are usually pronounceable, but keep in mind that this generator _has no bias_, and as such every single word and name could potentially come from it.

If you're running from cli.py, make sure the CONFIG_PATH (main.py, line 13) is set to RUN_CONFIG_PATH.

To build, run:

    pyinstaller cli.py --name namegenerator --onefile -w

Or leave out the `-w` for debug.

If it's having trouble finding the config file, add the following lines to namegenerator.spec:

    import shutil
    
    shutil.copyfile('data/settings.ini', '{0}/settings.ini'.format(DISTPATH))

And rerun with:

    pyinstaller --clean namegenerator.spec
