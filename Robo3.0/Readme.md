Documentação do Projeto de Controle de Posição de Robô

Introdução:
O projeto Robô Digital tem por objetivo a elaboração de uma solução completa de integração entre as Tecnologias de Automação (TA) e as Tecnologias de informação (TI). Trata-se de uma representação digital para um braço robótico com conexão em tempo real com sua contrapartida no mundo real. Para a construção deste sistema, será necessário construir três elementos:
Backend: será necessário construir um backend capaz de armazenar informações como deslocamento do robô, sua posição e enviar informações em tempo real para um ambiente de simulação. Para interação com o backend, deve-se também construir uma API que permita o envio e recebimento de dados por clientes.
Frontend: para que o usuário possa interagir com o sistema, uma aplicação Frontend deve ser construída. Ela deve possibilitar que o usuário realize requisições de deslocamento do manipulador robótico. Os deslocamentos podem ser realizados tanto em espaço de juntas como coordenadas globais. Cada deslocamento deve ser armazenado. Deve ser possível visualizar a posição atual do robô pela interface.
Simulação: o sistema de simulação do comportamento robótico deve ser implementado utilizando uma representação tridimensional de sua cadeia cinemática. Recomenda-se a utilização da engine Godot para realizar esta implementação. O sistema de simulação deve realizar requisições para a API desenvolvida no sistema atualizar a posição-alvo do robô e receber sua posição atualizada. 

Tecnologias Utilizadas:

Framework Python Flask para o backend
Banco de dados SQLite para armazenar dados de posição do robô
HTML, CSS e JavaScript para o frontend
Godot, GdScript 

Endpoints da API:

GET /robot_position: Retorna a posição atual do robô em formato JSON.
POST /move_forward: Move o robô uma unidade para frente no eixo x.
POST /move_backward: Move o robô uma unidade para trás no eixo x.
POST /move_down: Move o robô uma unidade para baixo no eixo z.
POST /move_right: Move o robô uma unidade para a direita no eixo y.
POST /move_left: Move o robô uma unidade para a esquerda no eixo y.
POST /move_up: Move o robô uma unidade para cima no eixo z.

Frontend:
O frontend da aplicação consiste em um único arquivo HTML (index.html) que contém botões para controlar o movimento do robô. Os botões estão vinculados a funções JavaScript que fazem solicitações AJAX para os endpoints da API do backend.

Backend:
O backend da aplicação é construído usando o framework Python Flask. Ele consiste em um único arquivo Python (app.py) que define os endpoints da API e se conecta ao banco de dados SQLite para recuperar e atualizar os dados de posição do robô. Alem disso ele retorna o frontend utilizando a função send_file('front\index.html') do Flask.

Banco de Dados:
O banco de dados SQLite (position.db) armazena a posição atual do robô em três dimensões (x, y e z). Cada mudança de posição do robô resulta em uma nova linha sendo inserida na tabela "position" com um novo ID. Cada linha representa uma posição diferente do robô, com o ID sendo incrementado a cada nova inserção.

Simulação:
A simulacao foi feita na Engine Godot e contém uma cena 3D com um nó CanvasLayer, um MeshInstance e um HTTPRequest. O MeshInstance representa o robô na cena e o HTTPRequest é usado no codigo do CanvasLayer para fazer uma solicitação HTTP para o servidor e receber a posição atual do robô em formato JSON. Em seguida, a posição do robô é atualizada na cena 3D usando a transformação do nó MeshInstance. E por fim, o código é executado continuamente para garantir que a posição do robô seja sempre atualizada na cena, permitindo que o robô se mova suavemente na cena 3D.

