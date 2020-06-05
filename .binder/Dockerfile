#From a genie application container
#copy the application into an OU customised notebook container
#and use nbserverproxy to run the genie application

FROM ouimd/genie_app

FROM ousefulcoursecontainers/oubrandednotebook

USER root
RUN apt update \
    && apt-get install -y curl \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs

USER $NB_USER
WORKDIR $HOME
COPY --from=0 /home/genie/node_app ./genie/

RUN pip install --no-cache jupyter-server-proxy 
#RUN pip install --no-cache numpy matplotlib ipywidgets

ADD .jupyter/jupyter_notebook_config.py $HOME/.jupyter/jupyter_notebook_config.py
#COPY notebooks/*.ipynb /home/${NB_USER}