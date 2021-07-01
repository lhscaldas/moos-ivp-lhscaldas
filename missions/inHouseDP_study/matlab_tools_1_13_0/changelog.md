## Versões
1.13.0 (22/12/2020)
  - Added Python wrapper py4j
        
1.11.1 (27/02/2020)
  - Gerad com a versão 8.4.5 do Buzz
        
1.11.0 (05/02/2019)
  - GUI for thruster control
        
1.10.1 (27/03/2019)
  - Gerado com a versão 8.2.8 do Buzz

1.10.0 (03/12/2018)
  - HDF5 integrado

1.8.1 (09/08/2018)
  - Gerado com a versão 8.1.0 do Buzz
  
1.8.0 (15/05/2018)
  - Gets session without need of scenario

1.7.0 (14/05/2018)
  - Callback para scenario implementado

1.6.6 (23/03/2018)
  - Gerado com a versão 7.5.2 do Buzz

1.6.5 (19/03/2018)
  - Gerado com a versão 7.5.1 do Buzz

1.6.4 (19/03/2018)
  - Gerado com a versão 7.5.0 do Buzz

1.6.3 (06/02/2018)
  - Gerado com a versão 7.4.0 do Buzz

1.6.2 (02/01/2018)
  - Gerado com a versão 7.3.0 do Buzz

1.6.1 (07/12/2017)
  - Gerado com a versão 7.2.0 do Buzz

1.6.0 (10/11/2017)
  - Remoção dos callbacks de evento com elementos visando econômia de memória

1.5.1 (09/11/2017)
  - Gerado com a versão 7.1.0 do Buzz
  
1.5.0 (25/09/2017)
  - Adicionado o evento TimeAdvanceRequested

1.4.1 (19/09/2017)
  - Gerado com a versão 7.0.2 do Buzz
  
1.4.0 (11/08/2017)
  - Possibilidade de alocação individual por cada grau de liberdade (Surge, Sway e Yaw)
  - Gerado com a versão 1.4.1 da Libtpn
  - Gerado com a versão 7.0.1 do Buzz
  
1.3.1 (07/08/2017)
  - Gerado com a versão 7.0.1 do Buzz
  - Gerado com a versão 1.4.1 da Libtpn
  - Acerto do cmake para manipular a libtpn de forma correta, dado o parametro LIBTPN_ROOT

1.3.0 (06/07/2017)
  - Gerado com a versão 7.0.0 do Buzz

1.2.2 (05/07/2017)
  - Gerado com a versão 6.11.1 do Buzz
  - Adicionado callbacks para: StateChangedEvent, NetworkChangedEvent e ErrorReportedEvent

1.2.1 (08/03/2017)
  - Atualização para Buzz 6.9.0

1.2.0 (03/02/2017)
  - Pacote tpn.io: Biblioteca de io para Matlab contendo:
    -> A API do Buzz 6.8.0 para Matlab;
    -> Uma implementação do BuzzSubscriber em java que permite a execução dos callbacks do buzz no MATLAB;
    -> A API do MongoDB;
    -> A API do P3D;
  - Pacote tpn.dp: Biblioteca de controle contendo:
    -> Controlador PID;
    -> Alocação de empuxo baseado no método da Pseudo-inversa;
    -> Filtro de ondas (Notch de 6ª ordem);
    -> Interface gráfica simples de teste;
  - Pacote tpn.matrix: Biblioteca de calculo matricial para java contendo:
    -> Wrapper para as operações matriciais utilizando a implementação da biblioteca matricial apache;
    
