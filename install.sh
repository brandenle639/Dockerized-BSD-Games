apt-get update
apt-get install -y python3 bsdgames
#useradd -s /bin/bash -d /home/games -m games
mkdir -p /home/games
chown games:games /home/games
