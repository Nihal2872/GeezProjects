FROM vckyouubitch/geez:master

RUN git clone -b master https://github.com/Nihal2872/GeezProjects /home/geezprojects/ \
    && chmod 777 /home/geezprojects \
    && mkdir /home/geezprojects/bin/

CMD [ "bash", "start" ]
