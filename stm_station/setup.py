from setuptools import find_packages, setup

package_name = 'stm_station'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='athens',
    maintainer_email='athens@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'serial_node_pub_sub = stm_station.stm_serial_node_pub_sub:main',
            'serial_node_pub = stm_station.stm_serial_node_pub:main',
            'control_node_master_slave = stm_station.stm_control_node_master_slave:main',
            'control_node_master_slave_poscontrol = stm_station.stm_control_node_master_slave_poscontrol:main'
        ],
    },
)
