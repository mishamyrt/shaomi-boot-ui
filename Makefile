dist:
	mkdir -p dist

all: bootanimation logo

bootanimation: dist
	cd bootanimation; zip -0 bootanimation.zip desc.txt part0/*
	mv bootanimation/bootanimation.zip magisk-module/system/media/
	cd magisk-module; zip -r shaomi.zip ./*
	mv magisk-module/shaomi.zip dist/shaomi-bootanimation.zip
	rm magisk-module/system/media/bootanimation.zip

logo: dist
	python create-splash.py
	mv logo.img logo-installer/
	cd logo-installer; zip -r shaomi.zip ./*
	mv logo-installer/shaomi.zip dist/shaomi-logo.zip

.PHONY: bootanimation dist