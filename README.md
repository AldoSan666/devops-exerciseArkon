# Nombre del Proyecto
    Hello Matrix Counter
    
## Descripción
    -Pagina Hello World, con un contador POST , boton para reiniciarlo y responder GET's en JSON con los resultados actuales del contador.
    -El website cuenta con un estilo CSS y un HTML para layer frontal.
    -Esta imagen instala Flask y varios componentes de microframeworks para poder ejecutarse.
    -Contiene un Git workflow para CI/CD en la imagen de DockerHub, el trigger es un push a la rama.
    -Esto mantiene la imagen de Dockerhub al dia.
    -Esta imagen tiene la configuracion para desplegarse en clusteres de Kubernetes.
    
## Imagen de Docker
    https://hub.docker.com/r/aldosan666/flask-app

## Despliegue en Kubernetes
Para desplegar el servicio en un clúster de Kubernetes, utiliza los siguientes archivos:

    - k8s.yaml
    - El cluster fue probado en Minikube, el set up basico de minikube es requerido para que funcione bien ahi.
    - El cluster fue probado en AKS y queda operativo.
    - El cluster es de 3 replicas.

## Mejoras (Opcional)

    - Se agrega como se pide un contador de POSTS
    - Se agrega un boton de POST abajo del contador para incrementarlo
    - Se agrega un boton de CLEAR para reiniciarlo
    - Se agrega la funcion app-url:port/GET para entregar resultados del contador en JSON
    - Se agrega CSS y HTML
    - El siguiente codigo se agrego o modifico del principal: 

           [from flask import Flask, render_template, request, jsonify    # Agregado
            app = Flask(__name__, template_folder='templates')            # Agregado
            post_count = 0  
            
            @app.route('/', methods=['GET', 'POST'])                        # Agregado
            def index():
                global post_count
                if request.method == 'POST':
                    if 'reset' in request.form:
                        post_count = 0
                    else:
                        post_count += 1
                return render_template('index.html', post_count=post_count)
            
            @app.route('/post', methods=['POST'])                             # Agregado
            def handle_post(): 
                global post_count 
                post_count += 1 
                return "POST request received", 200
            
            @app.route('/get', methods=['GET'])                             # Agregado
            def handle_get():
                return jsonify({"post_count": post_count})]

## Enlaces

    - https://hub.docker.com/r/aldosan666/flask-app    --- DockerHub
    - https://github.com/AldoSan666/devops-exerciseArkon -- GitHub Repo


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ORIGINAL REQUEST------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Abraxas DevOps Exercise

## Intro

Thank you for your interest and participation in our recruitment process for our DevOps Engineer position, to continue with the process we ask you to take the following technical test and share your result with us.

If you have any questions or comments during the test, do not hesitate to contact us by email at reclutamiento@grupoabraxas.com

## Get your environment ready

You'll need:

1. A Github account
2. A docker hub account
3. Access to a kubernetes cluster for testing purposes (It can be Minikube or any other public or private option)
4. Fork this repository, then clone it locally.

## Ready for action?

Great!!
As a DevOps we need you to create a mechanism to deploy nanoservices. You'll be in charge of deploy, monitor, scale applications and promote the DevOps culture with the development team. But let's start by the begining, below you'll find the requirements for this test.

### Dockerize services

Dockerize the given service at [app.py](app.py), including all it's required dependencies installed and ready to rock.

### CI/CD

Implement a Github Actions workflow to build and publish your docker image on [docker hub](https://hub.docker.com/).

### Deployment

Create a service configuration file to deploy the service on your kubernetes cluster and expose it to the world.

### Extra Points

- Improve the given python service so it maintains a counter of the amount of **POST** requests it served, and return it on **GET** requests.

## Deliverables

- A link to the public docker registry where the image is published.

- A link to your repository containing:

    1. The Dockerfile(s) for the image(s).
    2. The kubernetes file(s) for the service deployment(s). The deployment should be replicable on our kubernetes cluster.
    3. Optionally the code for the improved version of the service.

## General Guidelines

Your code should be as simple as possible, yet well documented and robust.
Spend some time on designing your solution. Think about operational use cases from the real world. Few examples:

1. What happens if a service crashes?
2. How much effort will it take to create a new service? D.R.Y!

## Reference

- [Run a Stateless Application Using a Deployment](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)

