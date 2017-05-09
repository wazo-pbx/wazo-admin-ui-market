install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/market.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-market
	rm /etc/wazo-admin-ui/conf.d/market.yml
	systemctl restart wazo-admin-ui
