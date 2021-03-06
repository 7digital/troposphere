from setuptools import setup

setup(
    name='troposphere',
    version='1.9.4',
    description="AWS CloudFormation creation library",
    author="Mark Peek",
    author_email="mark@peek.org",
    url="https://github.com/cloudtools/troposphere",
    license="New BSD license",
    packages=['troposphere', 'troposphere.openstack', 'troposphere.helpers', 'troposphere.spotinst'],
    scripts=['scripts/cfn', 'scripts/cfn2py'],
    install_requires=["cfn_flip"],
    test_suite="tests",
    tests_require=["awacs"],
    extras_require={'policy': ['awacs']},
    use_2to3=True,
)
