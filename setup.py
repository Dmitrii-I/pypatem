"""Setup file."""

from setuptools import find_packages, setup

package_name = "pypatem"

if __name__ == "__main__":

    setup(
        name=package_name,
        description="Python project template",
        license="Proprietary",
        url="https://github.com/Dmitrii-I/pypatem",
        version="0.0.1",
        author="D. I.",
        author_email="foo@bar.com",
        keywords=["packaging"],
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        python_requires=">=3.8",
        install_requires=["sqlparse>=0.4.1,<1.0.0"],
        include_package_data=True,
    )
