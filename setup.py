import setuptools

setuptools.setup(
    # Needed to silence warnings
    name='seganalysis',
    url='https://github.com/The-Neuro-Bioinformatics-Core/seganalysis',
    author='Neuro Bioinformatics Core',
    maintainer='Saeid Amiri',
    author_email='saeid.amiri@mcgill.ca',
    packages=setuptools.find_packages(),
    install_requires=['numpy','pandas', 'hail'],
    # *strongly* suggested for sharing
    version='0.03',
    license='MIT'
)
