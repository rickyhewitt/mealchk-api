# mealchk-cli
# main.py
# ricky@rickyhewitt.dev
import sys
import importlib

import mealchk

def main():
    # Set the provider here
    # Valid values: local, gcloud, aws
    PROVIDER = 'local'

    # compile list of filenames
    filenames = []
    for arg in sys.argv[1:]:
        filenames.append(arg)

    # perform analysis on each filename
    for file_i in filenames:
        # TODO: Add support for http download
        # Import correct provider
        try:
            providermod = importlib.import_module('providers.%s' % PROVIDER)
        except ModuleNotFoundError:
            print('Error: Invalid provider specified. The \'%s\' provider could not be loaded.' % (PROVIDER))
            sys.exit()

        # Convert image to a string
        text = providermod.image_to_string(file_i)
        # print("Image analysis: ", text)
        # Perform analysis via mealchk
        mealchk.analyze(text)

if __name__=="__main__":
    main()