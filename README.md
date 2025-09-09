Este projeto é um sistema de revenda de carros desenvolvido em Python, utilizando o framework web Django (seguindo o padrão MVT - Model-View-Template) e PostgreSQL como banco de dados. O sistema permite o gerenciamento completo de veículos, desde a adição de novos carros ao catálogo até a exclusão de registros, passando pela visualização detalhada e atualização de informações. Uma funcionalidade inovadora é a integração com Inteligência Artificial, que gera automaticamente descrições para os carros quando estas não são fornecidas, otimizando o processo de cadastro e enriquecendo a apresentação dos veículos.

Tecnologias Utilizadas

O projeto foi construído com as seguintes tecnologias:

•
Python: Linguagem de programação principal.

•
Django: Framework web de alto nível para desenvolvimento rápido e seguro.

•
PostgreSQL: Sistema de gerenciamento de banco de dados relacional.

•
Inteligência Artificial (IA): Integrada para geração automática de descrições de veículos. (A IA específica utilizada é a Mistral AI, conforme identificado no arquivo requirements.txt e na estrutura de pastas mistralai_api.)

Funcionalidades

O sistema oferece as seguintes funcionalidades principais:

•
Adicionar Carro: Permite cadastrar novos veículos no sistema, incluindo informações como marca, modelo, ano, preço e, opcionalmente, uma descrição. Caso a descrição não seja fornecida, a IA integrada gerará uma automaticamente.

•
Listar Carros: Exibe uma lista completa dos veículos disponíveis no catálogo.

•
Ver Detalhes do Carro: Permite visualizar informações detalhadas de um veículo específico.

•
Atualizar Carro: Possibilita a edição das informações de um veículo já cadastrado.

•
Deletar Carro: Remove um veículo do catálogo do sistema.

•
Integração com IA: Geração automática de descrições para veículos sem descrição prévia.



