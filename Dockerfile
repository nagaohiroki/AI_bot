FROM ubuntu:latest
RUN apt-get update 
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN git clone https://github.com/nagaohiroki/AI_bot 
WORKDIR /AI_bot
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python3 ai_bot.py
