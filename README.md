# TCC - Instruções de instalação
A instalação deverá ser feita em SO Linux, preferencialmente Ubuntu. 
Também poderá ser realizada em WSL, mas requer o uso de um X Server para a visualização da simulação.
## MOOS-IvP
Executar os comandos no terminal do Linux

  $`svn co https://oceanai.mit.edu/svn/moos-ivp-aro/trunk/ moos-ivp`
  
  $`cd moos-ivp`
  
  $`svn update`
  
  $`sudo apt-get install  g++  cmake  xterm` 
  
  $`sudo apt-get install  libfltk1.3-dev  freeglut3-dev  libpng-dev  libjpeg-dev` 
  
  $`sudo apt-get install  libxft-dev  libxinerama-dev   libtiff5-dev`
  
  $`./build-moos.sh`
  
  $`./build-ivp.sh`
  
Adicionar a pasta MOOS-IvP/bin ao path do Linux, editando o arquivo .bashrc na pasta `/home/<username>` e inserindo as linhas:
  
   `PATH=$PATH:/home/<username>/moos-ivp/bin`
  
   `export PATH`
  
Testar:
  
  $`cd moos-ivp/ivp/missions/s1_alpha`
  
  $`pAntler --MOOSTimeWarp=10 alpha.moos`
  
## Pydyna
Clonar `$ git clone https://github.com/lhscaldas/pydyna.git`
  
Executar no terminal do Linux os seguintes comandos:
  
  $`python -m pip install -r requerimentos.txt`
  
  $`pip install pydyna-7.2.3-py3-none-linux_x86_64.whl`
  
A instalação deve ser feita em um venv com Python 3.6

## Pymoos
Executar os comandos no terminal do Linux, no mesmo venv do Pydyna:

  $`sudo apt-get install libboost-python-dev`
  
  $`git clone https://github.com/msis/python-moos`
  
  $`python3 setup.py build`
  
  $`python3 setup.py install`
  
## Testes
Efetuar o download deste repositório 

  $`git clone https://github.com/lhscaldas/moos-ivp-lhscaldas.git`

Para testar o pymoos, abrir a pasta plotter e dar permissão de execução ao arquivo plotter.py com o comando:

  $`chmod +x plotter.py`
  
Executar a missão alpha com o comando:

  $`pAntler alpha.moos`
  
Para testar a integração entre o MOOS-IvP e o Pydyna, abrir a pasta PID e dar permissão de execução aos arquivos iPydyna.py e pTrajectPID.py com o comando:

  $`chmod +x iPydyna.py`
  
  $`chmod +x pTrajectPID.py`
  
Executar a missão main com o comando:

  $`pAntler main.moos`
