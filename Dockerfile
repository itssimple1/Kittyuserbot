FROM itssimple1/kittyuserbot:latest

# clonning repo 
RUN git clone https://github.com/itssimple1/Kittyuserbot.git /root/userbot

RUN pip install --upgrade pip

# working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
