FROM debian:bookworm-slim
ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_FRONTEND teletype
COPY install.sh /install.sh
COPY start.sh /start.sh
COPY mnu.py /mnu.py
RUN /install.sh || true
RUN rm -r /install.sh
USER games
CMD /start.sh 
