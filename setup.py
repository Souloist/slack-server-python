from setuptools import find_packages, setup

third_party_dependencies = (
    "Flask",
    "flask-GraphQL",
    "psycopg2",
    "SQLAlchemy",
    "requests",
    "graphene_sqlalchemy",
)

tests_require = (
    "nose",
)

setup(
    name="slack-server-python",
    version="0.1.0",
    author="Richard Shen",
    author_email="rich.shen@nyu.edu",
    description="Slack clone backend",
    long_description=open("README.md").read(),
    packages=find_packages(exclude=["ez_setup"]),
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    install_requires=third_party_dependencies,
    test_require=tests_require,
    classifiers=[
        "Framework :: Flask",
        "Programming Language :: Python",
    ],
)
