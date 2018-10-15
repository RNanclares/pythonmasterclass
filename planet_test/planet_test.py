# import subprocess
# import sys
#
# reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
# installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
#
# print(installed_packages)
import ee from planet
ee.Initialize()
planetscope=ee.ImageCollection("projects/sat-io/terra2018/ps4b")

##you can even check how many images does the collection have
print(planetscope.size().getInfo())
