if [ ! -f deployment.phar ]; then
	wget https://github.com/dg/ftp-deployment/releases/download/v2.5/deployment.phar
fi

docker build -t deployer .

docker run --rm -it -v `pwd`:/work -w /work deployer sh -c 'cp -R sample.scraping-book.com / && php deployment.phar deployment.ini'
# php deployment.phar deployment.ini
