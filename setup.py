from setuptools import find_packages
from setuptools import setup

package_name = 'rqt_console'

setup(
    name=package_name,
    version='1.1.1',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/resource',
            ['resource/console_settings_dialog.ui',
             'resource/console_widget.ui',
             'resource/text_browse_dialog.ui']),
        ('share/' + package_name + '/resource/filters',
            ['resource/filters/custom_filter_widget.ui',
             'resource/filters/filter_wrapper_widget.ui',
             'resource/filters/custom_filter_widget.ui',
             'resource/filters/text_filter_widget.ui',
             'resource/filters/time_filter_widget.ui']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Aaron Blasdel',
    maintainer='Dirk Thomas, Aaron Blasdel',
    maintainer_email='dthomas@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'RQT plugin for monitoring ROS processes.'
    ),
    license='BSD',
    entry_points={
        'console_scripts': [
            'rqt_console = ' + package_name + '.main:main',
        ],
    },
)
