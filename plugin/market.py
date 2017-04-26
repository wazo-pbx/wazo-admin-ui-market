
MARKETS = {}

_markets = [
    ('user', 'Users', 'aqua', ['beta', 'users', 'tag1', 'tag2'], False, True, 'https://github.com/wazo-pbx/wazo-admin-ui-user', 'wazo-admin-ui-user', 'Francois Blackburn'),
    ('users', 'Groups', 'aqua', ['beta', 'users'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-group', 'wazo-admin-ui-group', 'Sylvain Boily'),
    ('compress', 'Conferences', 'yellow', ['beta', 'application'], True, False, 'https://github.com/wazo-pbx/wazo-admin-ui-conference', 'wazo-admin-ui-conference', 'Wazo Team'),
    ('automobile', 'Parking', 'yellow', ['beta', 'application'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-parking-lot', 'wazo-admin-ui-parking-lot', 'Wazo Team'),
    ('desktop', 'Switchboard', 'yellow', ['beta', 'application'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-switchboard', 'wazo-admin-ui-switchboard', 'Wazo Team'),
    ('envelope', 'Voicemail', 'yellow', ['beta', 'application'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-voicemail', 'wazo-admin-ui-voicemail', 'Wazo Team'),
    ('newspaper-o', 'CDR', 'yellow', ['beta', 'application'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-cdr', 'wazo-admin-ui-cdr', 'Wazo Team'),
    ('long-arrow-right', 'Incalls', 'green', ['beta', 'routing'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-incall', 'wazo-admin-ui-incall', 'Wazo Team'),
    ('long-arrow-left', 'Outcalls', 'green', ['beta', 'routing'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-outcall', 'wazo-admin-ui-outcall', 'Wazo Team'),
    ('bullhorn', 'Paging', 'yellow', ['beta', 'application'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-paging', 'wazo-admin-ui-paging', 'Wazo Team'),
    ('music', 'Moh', 'yellow', ['beta', 'application'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-moh', 'wazo-admin-ui-moh', 'Wazo Team'),
    ('server', 'Trunks', 'green', ['beta', 'routing'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-trunk', 'wazo-admin-ui-trunk', 'Wazo Team'),
    ('gears', 'Extensions', 'red', ['beta', 'internal'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-extension', 'wazo-admin-ui-extension', 'Wazo Team'),
    ('gears', 'Context', 'red', ['beta', 'internal'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-context', 'wazo-admin-ui-context', 'Wazo Team'),
    ('navicon', 'IVR', 'yellow', ['beta', 'application'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-ivr', 'wazo-admin-ui-ivr', 'Wazo Team'),
    ('gear', 'Devices', 'red', ['beta', 'internal'], False, False, 'https://github.com/wazo-pbx/wazo-admin-ui-device', 'wazo-admin-ui-device', 'Wazo Team'),
]

market_entry = []
for entry in _markets:
  market_entry.append({
      'icon': entry[0],
      'name': entry[1],
      'color': entry[2],
      'tags': entry[3],
      'on_installation': entry[4],
      'is_installed': entry[5],
      'url': entry[6],
      'plugin_name': entry[7],
      'author': entry[8]
  })

MARKETS.update({'items': market_entry})
