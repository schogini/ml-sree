

# python -m pip show scikit-learn  # to see which version and where scikit-learn is installed
# python -m pip freeze  # to see all packages installed in the active virtualenv
# python -c "import sklearn; sklearn.show_versions()"


mkdir -p lib

# pip3 install -t lib numpy pandas 
# pip3 install -t lib -U scikit-learn
# pip3 install -t lib -U matplotlib
pip3 install -t lib -U seaborn
