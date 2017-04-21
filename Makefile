install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/plugin.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-plugin
	rm /etc/wazo-admin-ui/conf.d/plugin.yml
	systemctl restart wazo-admin-ui
