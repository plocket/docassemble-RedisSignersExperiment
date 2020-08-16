import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.RedisSignersExperiment',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description="Trying out Redis as a way to get remote signatures more easily. It's an alternative to using action arguments, `force_ask`, and such.\r\n\r\nTests I’ve thought of so far:\r\n1:\r\n1. User signs on computer\r\n1. Sends to both cosigners by email\r\n1. Both sign on computer\r\n2:\r\n1. User signs on phone and finishes on phone.\r\n1. Sends to both cosigners by text\r\n1. Both sign on phone\r\n3:\r\n1. User says they’ll sign on phone\r\n1. User changes their mind before opening the site\r\n1. User signs on the computer\r\n1. Sends to both cosigners by email\r\n1. Cosigner 1 signs on computer\r\n1. Cosigner 2 signs on phone\r\n4:\r\n1. User says they’ll sign on phone\r\n1. User goes to first page of site on phone\r\n1. User changes their mind\r\n1. User signs on a different phone\r\n1. User finishes on computer\r\n1. User texts both cosigners\r\n1. Cosigner 1 says they’re not willing.\r\n1. Cosigner 1 visits the site again on computer and signs on computer.\r\n1. Cosigner 2 whatever\r\n5:\r\n1. User says they’ll sign on phone\r\n1. gets to signature on phone\r\n1. user changes their mind\r\n1. user signs on computer\r\n1. Tries to sign on phone, but instead taken to… not sure. ‘Finish on phone?’ question?\r\n1. User emails both cosigners\r\n1. Cosigner 1 says they’re not willing\r\n1. Cosigner 1 visits the site again on phone and signs on phone\r\n1. Cosigner 2 whatever\r\n6:\r\n1. User says they’ll sign on phone\r\n1. User signs on phone\r\n1.  User changes their mind and is taken to the page to send link to cosigners (because already have signature)\r\n1. User emails both cosigners\r\n1. Cosigner 1 starts on computer\r\n1. Cosigner 1 switches to phone\r\n1. Cosigner 1 signs on phone\r\n1. Cosigner 1 changes mind and tries to sign on computer\r\n1. Cosigner 1 taken to final page instead\r\n1. Cosigner 2 whatever\r\n7:\r\n1. User says they’ll sign on phone, signs on phone, but tries to change their mind and is taken to the ‘done’ page (because they’ve already signed)\r\n1. Cosigners do whatever\r\n8:\r\n1. User says to sign on phone\r\n1. User signs and moves on to emails\r\n1. User tries to continue on computer and… what happens?\r\n1. Cosigners do whatever",
      long_description_content_type='text/markdown',
      author='',
      author_email='52798256+plocket@users.noreply.github.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['docassemble.MAVirtualCourt'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/RedisSignersExperiment/', package='docassemble.RedisSignersExperiment'),
     )

