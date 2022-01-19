#!/usr/bin/bash

MODDIR="${NOTEBOOK}/etc/requirements.txt"
INSTALL_DIRECTORY='/usr/bin'

# This installs the specified version of python and the desired modules

set_version() {
    PYV=$1
    PYVS=$(echo ${PYV} | head -c 3)
    echo "setting the version to ${PYV}"
}

setup_system() {
    echo 'Installing requirements...'
    sudo apt-get update
    sudo apt-get install build-essential
    # sudo yum groupinstall "Development Tools"
    # sudo yum install gcc openssl-devel bzip2-devel libffi-devel
}

install_python_source() {
    echo "Downloading python version ${PYV}"
    cd ${INSTALL_DIRECTORY}
    sudo wget https://www.python.org/ftp/python/${PYV}/Python-${PYV}.tgz
    sudo tar xzf Python-${PYV}.tgz

    echo ''

    echo "Installing python"
    cd Python-${PYV}
    sudo ./configure --enable-optimizations
    sudo make altinstall
    sudo rm ${INSTALL_DIRECTORY}/Python-${PYV}.tgz

    echo ''

    echo "Verify version matches ${PYVS}"
    python${PYVS} -V
}

install_pip_requirements() {
    echo 'Updating pip'
    # sudo apt install python3-pip
    python${PYVS} -m pip install --upgrade pip

    echo ''

    echo 'Installing requirements file'
    python${PYVS} -m pip install --no-cache-dir -r $MODDIR
    # To find where mods are stored, run python<version> -m site
}

uninstall_python_version() {
    echo 'Uninstalling python and modules'
    sudo rm -f /usr/local/bin/python${PYVS}
    sudo rm -f /usr/local/bin/python${PYVS}-config
    sudo rm -f /usr/local/bin/pip${PYVS}
    sudo rm -rf /usr/local/lib/python${PYVS}
    sudo rm -rf $HOME/.local/lib/python${PYVS}
}

set_version '3.9.7'

if [ $# -ne 0 ]; then
    for arg in "$@"; do
        case $arg in
            3*)
                set_version $arg
                ;;

            install)
                echo "Python ${PYV} install only"
                setup_system
                install_python_source
                ;;

            mods)
                echo "Modules only for python ${PYV}"
                install_pip_requirements
                ;;

            uninstall)
                echo "Uninstalling Python ${PYV}"
                uninstall_python_version
                ;;
        esac
    done
else
    echo "Installing the Python ${PYV} and Modules"
    setup_system
    install_python_source
    install_pip_requirements
fi
