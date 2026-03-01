pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'pyquran'
gnome = import('gnome')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'pyquran.in',
  output: 'pyquran',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x'
)

pyquran_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'widgets/desktop_view.py',
  'widgets/mobile_view.py',
  'widgets/sidebar_list.py',
  'helpers/quran_data.py',
  'helpers/app_logic.py',
]

install_data(pyquran_sources, install_dir: moduledir)

