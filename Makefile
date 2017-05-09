install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/50-wazo-plugin-market.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-market
	rm /etc/wazo-admin-ui/conf.d/50-wazo-plugin-market.yml
	systemctl restart wazo-admin-ui
