# StepUP
Plataforma de gerenciamento de eventos apresentada para o Hackathon do VI CONPEX


# Install Django dependencies
`$ git clone https://github.com/drakcamicazi/stepup`<br>
`$ cd stepup`<br>
`$ python -m venv venv`<br>
`$ source ./venv/bin/activate`<br>
`(venv) $ pip install -r requirements.txt`

# Start Postgres Server (Docker)
`$ docker-compose up -d`

# Extra
Install on your SO: python-pygraphviz<br>
Ubuntu : `sudo apt-get install pygraphviz`<br>
Arch   : `yaourt -S pygraphviz`<br>

Generate UML Diagram of Django App<br>
`python manage.py graph_models -a -g -o app.png`