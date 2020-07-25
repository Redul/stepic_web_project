CONFIG = {
  'mode': 'wsgi',
  'working_dir': '/home/box/web/ask',
  'pythonpath': '/home/box/web/ask',
  'python': '/usr/bin/python3',
  'args': (
    '--bind=0.0.0.0:8080',
    '--workers=2',
    '--timeout=15',
    'ask.wsgi:application'
  )
}
