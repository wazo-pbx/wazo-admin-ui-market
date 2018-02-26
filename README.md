Plugin market for wazo-admin-ui

Install
-------

    make

Uninstall
---------

You need to have python-pip installed.

    make uninstall

Translations
------------

To extract new translations:

    % python setup.py extract_messages

To create new translation catalog:

    % python setup.py init_catalog -l <locale>

To update existing translations catalog:

    % python setup.py update_catalog

Edit file `wazo_admin_ui_market/translations/<locale>/LC_MESSAGES/messages.po` and compile
using:

    % python setup.py compile_catalog
